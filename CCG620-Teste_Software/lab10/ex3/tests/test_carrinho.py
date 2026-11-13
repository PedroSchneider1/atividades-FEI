import pytest
from carrinho import Carrinho


def carrinho_com(subtotal):
    c = Carrinho()
    c.adicionar(subtotal)
    return c


# --- mantidos da teoria ---
def test_carrinho_vazio_total_zero():
    assert Carrinho().total == 0


def test_um_item():
    assert carrinho_com(2500).total == 2500


def test_quantidade_dois():
    c = Carrinho()
    c.adicionar(2500, quantidade=2)
    assert c.total == 5000


def test_preco_minimo_valido_e_um():
    assert carrinho_com(1).total == 1


def test_varias_adicoes_acumulam_no_subtotal():
    c = Carrinho()
    c.adicionar(100)
    c.adicionar(200)
    assert c.total == 300


def test_preco_zero_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().adicionar(0)


def test_cupom_desconhecido_rejeitado():
    with pytest.raises(ValueError):
        Carrinho().aplicar_cupom("XYZ")


# --- reescritos para as regras novas ---
def test_dez_abaixo_do_minimo_nao_da_desconto():
    c = carrinho_com(5000)
    c.aplicar_cupom("DEZ")
    assert c.total == 5000


def test_cupom_aplicado_antes_vale_quando_o_subtotal_chega_ao_minimo():
    c = Carrinho()
    c.aplicar_cupom("DEZ")
    c.adicionar(1000)
    assert c.total == 1000
    c.adicionar(9000)  # subtotal 10000
    assert c.total == 9000


def test_dez_fronteira_9999_e_10000():
    a = carrinho_com(9999)
    a.aplicar_cupom("DEZ")
    b = carrinho_com(10000)
    b.aplicar_cupom("DEZ")
    assert (a.total, b.total) == (9999, 9000)


# --- VINTE ---
def test_vinte_fronteira_29999_e_30000():
    a = carrinho_com(29999)
    a.aplicar_cupom("VINTE")
    b = carrinho_com(30000)
    b.aplicar_cupom("VINTE")
    assert (a.total, b.total) == (29999, 24000)


# --- segundo cupom substitui o primeiro ---
def test_segundo_cupom_substitui_o_primeiro_dez_depois_vinte():
    c = carrinho_com(30000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")
    assert c.total == 24000


def test_segundo_cupom_substitui_o_primeiro_vinte_depois_dez():
    c = carrinho_com(30000)
    c.aplicar_cupom("VINTE")
    c.aplicar_cupom("DEZ")
    assert c.total == 27000


def test_segundo_cupom_abaixo_do_minimo_nao_herda_o_desconto_do_primeiro():
    c = carrinho_com(10000)
    c.aplicar_cupom("DEZ")
    c.aplicar_cupom("VINTE")
    assert c.total == 10000


# --- quantidade ---
@pytest.mark.parametrize("q", [0, -1, 1.5, 2.0, "2", True])
def test_quantidade_invalida_lanca_value_error(q):
    with pytest.raises(ValueError):
        Carrinho().adicionar(100, quantidade=q)


def test_quantidade_invalida_nao_altera_o_subtotal():
    c = carrinho_com(100)
    with pytest.raises(ValueError):
        c.adicionar(100, quantidade=0)
    assert c.total == 100


def test_quantidade_um_e_valida():
    c = Carrinho()
    c.adicionar(100, quantidade=1)
    assert c.total == 100
