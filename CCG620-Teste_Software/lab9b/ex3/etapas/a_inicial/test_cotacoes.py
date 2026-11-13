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
