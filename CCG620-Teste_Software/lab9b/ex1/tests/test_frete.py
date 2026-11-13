import pytest

from frete import modalidade_frete

# ---------------------------------------------------------------
# Testes ORIGINAIS (suite inicial do laboratorio)
# ---------------------------------------------------------------


def test_correio_expresso():
    assert modalidade_frete(5, 300) == "Correio expresso"


def test_correio_economico():
    assert modalidade_frete(2, 1000) == "Correio economico"


# ---------------------------------------------------------------
# Testes NOVOS: valor-limite em cada comparacao do codigo
# ---------------------------------------------------------------

# --- Validacao do PESO: valido de 0 (exclusivo) ate 30 (inclusivo) ---
@pytest.mark.parametrize("peso", [0, -1, 30.01, 31])
def test_peso_invalido_lanca_erro_com_mensagem_exata(peso):
    # peso=0 mata  "<= 0" -> "< 0"   (mutmut_2)
    # peso=-1 e 31 matam "or" -> "and" (mutmut_1)
    # peso=31 mata "> 30" -> "> 31"   (mutmut_5)
    # str(...) == msg mata ValueError(None) e todas as variacoes de texto
    with pytest.raises(ValueError) as erro:
        modalidade_frete(peso, 100)
    assert str(erro.value) == "Peso invalido"


def test_peso_minimo_valido():
    # peso=1 mata "<= 0" -> "<= 1" (mutmut_3): 1 tem que ser aceito
    assert modalidade_frete(1, 5) == "Motoboy"


def test_peso_maximo_valido_30():
    # peso=30 mata "> 30" -> ">= 30" (mutmut_4): 30 tem que ser aceito
    assert modalidade_frete(30, 5) == "Transportadora"


# --- Validacao da DISTANCIA: valido de 0 (inclusivo) ate 5000 (inclusivo) ---
@pytest.mark.parametrize("distancia", [-1, 5001])
def test_distancia_invalida_lanca_erro_com_mensagem_exata(distancia):
    # distancia=-1 mata "or" -> "and" (mutmut_10)
    # distancia=5001 mata "> 5000" -> "> 5001" (mutmut_14)
    with pytest.raises(ValueError) as erro:
        modalidade_frete(5, distancia)
    assert str(erro.value) == "Distancia invalida"


def test_distancia_zero_valida():
    # distancia=0 mata "< 0" -> "<= 0" (mutmut_11) e "< 0" -> "< 1" (mutmut_12)
    assert modalidade_frete(5, 0) == "Motoboy"


def test_distancia_5000_valida():
    # distancia=5000 mata "> 5000" -> ">= 5000" (mutmut_13)
    assert modalidade_frete(5, 5000) == "Correio economico"


# --- Fronteira de peso da Transportadora: acima de 20 ---
def test_peso_20_nao_e_transportadora():
    # peso=20 mata "> 20" -> ">= 20" (mutmut_19)
    assert modalidade_frete(20, 300) == "Correio expresso"


def test_peso_21_e_transportadora():
    # peso=21 mata "> 20" -> "> 21" (mutmut_20)
    assert modalidade_frete(21, 5) == "Transportadora"


def test_transportadora_texto_exato():
    # mata as 3 mutacoes de string de "Transportadora" (mutmut_21 a 23)
    assert modalidade_frete(25, 300) == "Transportadora"


# --- Fronteira de distancia do Motoboy: ate 10 ---
def test_distancia_10_e_motoboy():
    # distancia=10 mata "<= 10" -> "< 10" (mutmut_24)
    assert modalidade_frete(5, 10) == "Motoboy"


def test_distancia_11_e_correio_expresso():
    # distancia=11 mata "<= 10" -> "<= 11" (mutmut_25)
    assert modalidade_frete(5, 11) == "Correio expresso"


def test_motoboy_texto_exato():
    # mata as 3 mutacoes de string de "Motoboy" (mutmut_26 a 28)
    assert modalidade_frete(5, 3) == "Motoboy"


# --- Fronteira de distancia do Correio expresso: ate 500 ---
def test_distancia_500_e_correio_expresso():
    # distancia=500 mata "<= 500" -> "< 500" (mutmut_29)
    assert modalidade_frete(5, 500) == "Correio expresso"


def test_distancia_501_e_correio_economico():
    # distancia=501 mata "<= 500" -> "<= 501" (mutmut_30)
    assert modalidade_frete(5, 501) == "Correio economico"
