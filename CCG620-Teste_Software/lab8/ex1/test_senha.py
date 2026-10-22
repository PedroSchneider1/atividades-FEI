import pytest
from senha import forca

@pytest.mark.parametrize(
    "senha, esperado",
    [
        ("abc", "fraca"),          # caminho 1: len < 8
        ("abcdefg1!@", "forte"),   # caminho 2: len >= 8, pontos >= 4
        ("abcdefgh", "media"),     # caminho 3: len >= 8, pontos < 4
    ],
)
def test_forca(senha, esperado):
    assert forca(senha) == esperado
