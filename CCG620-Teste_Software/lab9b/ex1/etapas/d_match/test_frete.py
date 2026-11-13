import pytest

from frete import modalidade_frete

# VERSAO DO ITEM (d): troca  str(erro.value) == msg
#                     por    pytest.raises(ValueError, match=msg)
# Todo o resto e identico a etapa c_final.


def test_correio_expresso():
    assert modalidade_frete(5, 300) == "Correio expresso"


def test_correio_economico():
    assert modalidade_frete(2, 1000) == "Correio economico"


@pytest.mark.parametrize("peso", [0, -1, 30.01, 31])
def test_peso_invalido_lanca_erro_com_match(peso):
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(peso, 100)


def test_peso_minimo_valido():
    assert modalidade_frete(1, 5) == "Motoboy"


def test_peso_maximo_valido_30():
    assert modalidade_frete(30, 5) == "Transportadora"


@pytest.mark.parametrize("distancia", [-1, 5001])
def test_distancia_invalida_lanca_erro_com_match(distancia):
    with pytest.raises(ValueError, match="Distancia invalida"):
        modalidade_frete(5, distancia)


def test_distancia_zero_valida():
    assert modalidade_frete(5, 0) == "Motoboy"


def test_distancia_5000_valida():
    assert modalidade_frete(5, 5000) == "Correio economico"


def test_peso_20_nao_e_transportadora():
    assert modalidade_frete(20, 300) == "Correio expresso"


def test_peso_21_e_transportadora():
    assert modalidade_frete(21, 5) == "Transportadora"


def test_transportadora_texto_exato():
    assert modalidade_frete(25, 300) == "Transportadora"


def test_distancia_10_e_motoboy():
    assert modalidade_frete(5, 10) == "Motoboy"


def test_distancia_11_e_correio_expresso():
    assert modalidade_frete(5, 11) == "Correio expresso"


def test_motoboy_texto_exato():
    assert modalidade_frete(5, 3) == "Motoboy"


def test_distancia_500_e_correio_expresso():
    assert modalidade_frete(5, 500) == "Correio expresso"


def test_distancia_501_e_correio_economico():
    assert modalidade_frete(5, 501) == "Correio economico"
