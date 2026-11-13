"""
Etapa (a): suite escrita por ANALISE DE VALOR-LIMITE, sem rodar nenhuma
ferramenta antes (so lendo a especificacao).

Especificacao:
  * dias fora de [0, 60]      -> ValueError
  * ate 5 dias                -> sem multa
  * a partir do 6o dia        -> 1% por dia alem do quinto
  * resultado arredondado a 2 casas

Particoes de 'dias':   [..., -1] | [0 .. 5] | [6 .. 60] | [61, ...]
Valores-limite:        -1, 0, 1  |  4, 5, 6 |  59, 60, 61  (+ um nominal: 30)
Usamos valor = 100 para facilitar as contas (1 dia de multa = R$ 1,00).
"""
import pytest

from multa import valor_com_multa


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
