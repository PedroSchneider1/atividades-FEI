import pytest

from parcelamento import parcela


# Partições da especificação para n:
#   inválido (n < 1) | 1..3 sem juros | 4..12 com juros de 2% por parcela além da 3ª | inválido (n > 12)
# Valores-limite: 0, 1, 2 | 2, 3, 4 | 11, 12, 13

@pytest.mark.parametrize("n", [0, 13])
def test_n_invalido(n):
    with pytest.raises(ValueError, match="parcelas invalidas"):
        parcela(100, n)


# (c) Acrescentado para matar parcelamento__mutmut_7 ("XXparcelas invalidasXX"):
#     match= usa re.search e aceita texto extra ao redor; a comparação exata não.
@pytest.mark.parametrize("n", [0, 13])
def test_n_invalido_mensagem_exata(n):
    with pytest.raises(ValueError) as exc:
        parcela(100, n)
    assert str(exc.value) == "parcelas invalidas"


def test_n_1_limite_inferior_valido():
    assert parcela(100, 1) == 100.0


def test_n_2_sem_juros():
    assert parcela(100, 2) == 50.0


def test_n_3_ultimo_sem_juros():
    assert parcela(100, 3) == 33.33


def test_n_4_primeiro_com_juros():
    # juros = 0.02 * (4-3) = 2% -> 102 / 4 = 25.5
    assert parcela(100, 4) == 25.5


def test_n_11_penultimo():
    # juros = 0.02 * 8 = 16% -> 116 / 11 = 10.545... -> 10.55
    assert parcela(100, 11) == 10.55


def test_n_12_limite_superior_valido():
    # juros = 0.02 * 9 = 18% -> 118 / 12 = 9.8333... -> 9.83
    assert parcela(100, 12) == 9.83


# ---------------------------------------------------------------------------
# Vivo EQUIVALENTE (não há teste que o mate):
#   parcelamento__mutmut_9 : "if n <= 3" -> "if n < 3"
#   Só n == 3 muda de ramo, e nele o else dá juros = 0.02 * (3 - 3) = 0,
#   exatamente o valor que o ramo "then" atribuiria. Mesmo estado, mesma saída.
# ---------------------------------------------------------------------------
