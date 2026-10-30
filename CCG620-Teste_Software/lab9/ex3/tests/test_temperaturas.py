import pytest

from temperaturas import dia_do_maior, maior


# ===========================================================================
# Suíte inicial (enunciado): listas [21,25,19,30,22], [18] e [30,21]
# com valor exato + lista vazia com pytest.raises sem conferir a mensagem
# ===========================================================================
def test_maior_lista_semana():
    assert maior([21, 25, 19, 30, 22]) == 30


def test_maior_um_elemento():
    assert maior([18]) == 18


def test_maior_dois_elementos():
    assert maior([30, 21]) == 30


def test_maior_lista_vazia():
    with pytest.raises(ValueError):
        maior([])


def test_dia_do_maior_lista_semana():
    assert dia_do_maior([21, 25, 19, 30, 22]) == 3


def test_dia_do_maior_um_elemento():
    assert dia_do_maior([18]) == 0


def test_dia_do_maior_dois_elementos():
    assert dia_do_maior([30, 21]) == 0


def test_dia_do_maior_lista_vazia():
    with pytest.raises(ValueError):
        dia_do_maior([])


# ===========================================================================
# Item (c): testes que matam os vivos NÃO equivalentes
# ===========================================================================

# --- mensagem de erro (maior_2/3/4 e dia_do_maior_2/3/4) -------------------
# Comparação exata (não use match= sem âncoras: "XXlista vaziaXX" passaria).
def test_maior_lista_vazia_mensagem():
    with pytest.raises(ValueError) as exc:
        maior([])
    assert str(exc.value) == "lista vazia"


def test_dia_do_maior_lista_vazia_mensagem():
    with pytest.raises(ValueError) as exc:
        dia_do_maior([])
    assert str(exc.value) == "lista vazia"


# --- maior_7: temps[1:] -> temps[2:]  ---------------------------------------
# O maior está na posição 1; se o laço pular o índice 1, o resultado é 21.
def test_maior_esta_na_segunda_posicao():
    assert maior([21, 30]) == 30


# --- dia_do_maior_11: range(1, n) -> range(2, n) ----------------------------
# O maior está na posição 1; se o laço pular o índice 1, o resultado é 0.
def test_dia_do_maior_esta_na_segunda_posicao():
    assert dia_do_maior([21, 30, 19]) == 1


# --- dia_do_maior_12: ">" -> ">=" -------------------------------------------
# Empate no máximo: a especificação pede o PRIMEIRO dia (posição 0, não 2).
def test_dia_do_maior_empate_devolve_o_primeiro():
    assert dia_do_maior([30, 21, 30]) == 0


# ===========================================================================
# Vivos EQUIVALENTES (não há teste que os mate):
#   maior__mutmut_8        : "if t > m"  -> "if t >= m"
#   dia_do_maior__mutmut_9 : range(1, n) -> range(0, n)  (range(len(temps)))
# ===========================================================================
