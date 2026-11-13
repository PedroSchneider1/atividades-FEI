import pytest

from cotacoes import dia_da_compra, menor_preco


# ----------------------------- menor_preco -----------------------------
def test_menor_preco_lista_variada():
    assert menor_preco([32, 28, 35, 25, 30]) == 25


def test_menor_preco_um_elemento():
    assert menor_preco([40]) == 40


def test_menor_preco_dois_elementos():
    assert menor_preco([20, 27]) == 20


def test_menor_preco_lista_vazia():
    with pytest.raises(ValueError):  # sem conferir a mensagem
        menor_preco([])


# >>> NOVOS (etapa c): matam os mutantes NAO equivalentes <<<
def test_menor_preco_lista_vazia_mensagem_exata():
    # mata ValueError(None), "XXsem cotacoesXX" e "SEM COTACOES"
    with pytest.raises(ValueError) as erro:
        menor_preco([])
    assert str(erro.value) == "sem cotacoes"


def test_menor_preco_minimo_na_segunda_posicao():
    # mata  precos[1:] -> precos[2:]  (o 2o elemento nunca era examinado)
    assert menor_preco([30, 20, 25]) == 20


# ----------------------------- dia_da_compra ---------------------------
def test_dia_da_compra_lista_variada():
    assert dia_da_compra([32, 28, 35, 25, 30]) == 3


def test_dia_da_compra_um_elemento():
    assert dia_da_compra([40]) == 0


def test_dia_da_compra_dois_elementos():
    assert dia_da_compra([20, 27]) == 0


def test_dia_da_compra_lista_vazia():
    with pytest.raises(ValueError):  # sem conferir a mensagem
        dia_da_compra([])


# >>> NOVOS (etapa c): matam os mutantes NAO equivalentes <<<
def test_dia_da_compra_lista_vazia_mensagem_exata():
    with pytest.raises(ValueError) as erro:
        dia_da_compra([])
    assert str(erro.value) == "sem cotacoes"


def test_dia_da_compra_minimo_na_segunda_posicao():
    # mata  range(1, n) -> range(2, n)  (indice 1 nunca era examinado)
    assert dia_da_compra([30, 20, 25]) == 1


def test_dia_da_compra_empate_devolve_o_ultimo_dia():
    # mata  <= -> <   (a especificacao pede o ULTIMO dia com o menor preco)
    assert dia_da_compra([20, 30, 20]) == 2


def test_dia_da_compra_empate_consecutivo():
    assert dia_da_compra([25, 25]) == 1
