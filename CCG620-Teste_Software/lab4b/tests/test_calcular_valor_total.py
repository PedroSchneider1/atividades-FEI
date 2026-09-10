from src.calcular_valor_total import calcular_valor_total
import pytest

@pytest.fixture
def valores_exemplo():
    return [11.99, 10]

def test_calcular_valor_total_fixture(valores_exemplo):
    assert calcular_valor_total(valores_exemplo[0], valores_exemplo[1]) == 119.9
    assert calcular_valor_total(valores_exemplo[0], valores_exemplo[1]) == 129.9 # teste negativo

@pytest.mark.parametrize("preco, qtd, esperado",[
    (10, 2, 20),
    (12.99, 1, 12.99),
    (100, 2, 200),
])
def test_calcular_valor_total_parametrize(preco, qtd, esperado):
    assert calcular_valor_total(preco, qtd) == esperado

