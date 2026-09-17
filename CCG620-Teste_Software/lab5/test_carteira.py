import os
import pytest

from carteira import (
    CarteiraDigital,
    SaldoInsuficienteError,
    classificar_transacao,
    transferir,
)

# ---------------------------------------------------------------------------
# 1) saldo inicial, depósito e saque dentro do saldo disponível
# ---------------------------------------------------------------------------

def test_saldo_inicial_padrao():
    carteira = CarteiraDigital()

    assert carteira.saldo == 0


def test_saldo_inicial_customizado():
    saldo_inicial = 150

    carteira = CarteiraDigital(saldo_inicial=saldo_inicial)

    assert carteira.saldo == 150


def test_depositar_soma_ao_saldo(tmp_path):
    log_path = tmp_path / "carteira.log"
    carteira = CarteiraDigital(saldo_inicial=100, log_path=str(log_path))

    carteira.depositar(50)

    assert carteira.saldo == 150


def test_sacar_dentro_do_saldo_disponivel(tmp_path):
    log_path = tmp_path / "carteira.log"
    carteira = CarteiraDigital(saldo_inicial=200, log_path=str(log_path))

    carteira.sacar(80)

    assert carteira.saldo == 120


# ---------------------------------------------------------------------------
# 2) Testes da exceção SaldoInsuficienteError
# ---------------------------------------------------------------------------

def test_sacar_valor_maior_que_saldo_levanta_excecao(tmp_path):
    log_path = tmp_path / "carteira.log"
    carteira = CarteiraDigital(saldo_inicial=50, log_path=str(log_path))

    with pytest.raises(SaldoInsuficienteError) as exc_info:
        carteira.sacar(100)

    assert exc_info.type is SaldoInsuficienteError
    assert str(exc_info.value) == "saldo insuficiente"


def test_saldo_nao_muda_apos_saque_invalido(tmp_path):
    log_path = tmp_path / "carteira.log"
    carteira = CarteiraDigital(saldo_inicial=50, log_path=str(log_path))

    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(100)

    assert carteira.saldo == 50


# ---------------------------------------------------------------------------
# 3) Fixture com setup/teardown do arquivo de log
# ---------------------------------------------------------------------------

LOG_PATH = "carteira.log"


@pytest.fixture
def carteira_com_log():
    # Setup: garante que não sobrou log de uma execução anterior
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)

    carteira = CarteiraDigital(saldo_inicial=0)  # usa o log_path padrão

    yield carteira

    # Teardown: roda mesmo se o teste falhar (código após o yield sempre
    # executa, pois o pytest trata a fixture como um gerenciador de contexto)
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)


def test_deposito_grava_linha_no_log(carteira_com_log):
    carteira = carteira_com_log

    carteira.depositar(75)

    with open(LOG_PATH, "r") as f:
        conteudo = f.read()
    assert conteudo == "deposito:75\n"


# ---------------------------------------------------------------------------
# 4) Teste parametrizado de classificar_transacao
# ---------------------------------------------------------------------------
#
# BUG ENCONTRADO na primeira versão da função:
#
#     def classificar_transacao(valor):
#         if valor < 100:
#             return "pequena"
#         elif valor <= 1000:          # <-- usava "<=" em vez de "<"
#             return "media"
#         else:
#             return "grande"
#
# Com "elif valor <= 1000", o caso valor=1000 caía nessa condição
# (1000 <= 1000 é True) e a função retornava "media". Mas a especificação
# diz que 1000 deve ser "grande".
# O caso de teste com id "limite_1000_e_grande" falhava por causa disso.
#
# Correção aplicada em carteira.py: trocar "<=" por "<" na segunda condição,
# de forma que 1000 caia no "else" e seja classificado como "grande".
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0, "pequena"),
        (99, "pequena"),
        (100, "media"),
        (500, "media"),
        (999, "media"),
        (1000, "grande"),
        (1500, "grande"),
    ],
    ids=[
        "valor_zero_e_pequena",
        "limite_99_ainda_pequena",
        "limite_100_e_media",
        "valor_intermediario_e_media",
        "limite_999_ainda_media",
        "limite_1000_e_grande",
        "valor_bem_acima_e_grande",
    ],
)
def test_classificar_transacao(valor, esperado):
    resultado = classificar_transacao(valor)

    assert resultado == esperado


# ---------------------------------------------------------------------------
# 5) Suíte de testes de transferir(origem, destino, valor)
# ---------------------------------------------------------------------------

@pytest.fixture
def par_de_carteiras(tmp_path):
    """Cria duas carteiras: origem com saldo e destino vazia."""
    log_origem = tmp_path / "origem.log"
    log_destino = tmp_path / "destino.log"

    origem = CarteiraDigital(saldo_inicial=500, log_path=str(log_origem))
    destino = CarteiraDigital(saldo_inicial=0, log_path=str(log_destino))

    return origem, destino


@pytest.mark.parametrize(
    "valor_transferido",
    [50, 200, 500],
    ids=[
        "transferencia_de_valor_pequeno",
        "transferencia_de_valor_medio",
        "transferencia_de_todo_o_saldo",
    ],
)
def test_transferir_com_sucesso(par_de_carteiras, valor_transferido):
    origem, destino = par_de_carteiras
    saldo_origem_inicial = origem.saldo
    saldo_destino_inicial = destino.saldo

    transferir(origem, destino, valor_transferido)

    assert origem.saldo == saldo_origem_inicial - valor_transferido
    assert destino.saldo == saldo_destino_inicial + valor_transferido


def test_transferir_valor_maior_que_saldo_nao_altera_nenhuma_carteira(par_de_carteiras):
    origem, destino = par_de_carteiras
    saldo_origem_inicial = origem.saldo
    saldo_destino_inicial = destino.saldo
    valor_maior_que_o_saldo = saldo_origem_inicial + 1000

    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, valor_maior_que_o_saldo)

    assert origem.saldo == saldo_origem_inicial
    assert destino.saldo == saldo_destino_inicial
