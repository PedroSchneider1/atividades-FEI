import pytest

from multa import valor_com_multa

# ===============================================================
# Parte 1: suite por ANALISE DE VALOR-LIMITE (etapa a) - inalterada
# ===============================================================


# --- limites da VALIDACAO (invalido: dias < 0 ou dias > 60) ---
@pytest.mark.parametrize("dias", [-1, 61])
def test_dias_invalidos_lancam_erro(dias):
    with pytest.raises(ValueError):
        valor_com_multa(100, dias)


# --- faixa SEM multa: 0 a 5 dias ---
@pytest.mark.parametrize("dias", [0, 1, 4, 5])
def test_ate_cinco_dias_sem_multa(dias):
    assert valor_com_multa(100, dias) == 100.0


# --- faixa COM multa: 6 a 60 dias ---
def test_seis_dias_um_por_cento():
    assert valor_com_multa(100, 6) == 101.0


def test_trinta_dias_nominal():
    assert valor_com_multa(100, 30) == 125.0


def test_cinquenta_e_nove_dias():
    assert valor_com_multa(100, 59) == 154.0


def test_sessenta_dias_maximo_valido():
    assert valor_com_multa(100, 60) == 155.0


# ===============================================================
# Parte 2: testes NOVOS (etapa c) - matam os vivos NAO equivalentes
# ===============================================================
@pytest.mark.parametrize("dias", [-1, 61])
def test_mensagem_de_erro_exata(dias):
    # mata ValueError(None), "XXatraso invalidoXX" e "ATRASO INVALIDO"
    # (os 3 mutantes de mensagem sobreviviam porque o teste so checava o TIPO)
    with pytest.raises(ValueError) as erro:
        valor_com_multa(100, dias)
    assert str(erro.value) == "atraso invalido"


def test_arredondamento_em_duas_casas():
    # 123.45 * 1.02 = 125.91900000000001
    #   round(t, 2) -> 125.92   (correto)
    #   round(t, 3) -> 125.919  (mutante)
    #   round(t)    -> 126      (mutantes round(total, None) e round(total, ))
    # Com valor = 100 o resultado ja tinha so 1 casa e o round() nao
    # "infectava" o estado: por isso 3 mutantes sobreviviam ao BVA.
    assert valor_com_multa(123.45, 7) == 125.92


# ---------------------------------------------------------------
# NAO existe teste para o mutante  `dias <= 5` -> `dias < 5`.
# Ele e EQUIVALENTE: para dias == 5 o ramo else calcula
#   multa = 0.01 * (5 - 5) = 0.0   -> mesmo valor que `multa = 0`.
# (diferenca so no TIPO: 100 vs 100.0, fora do que a especificacao exige)
# ---------------------------------------------------------------
