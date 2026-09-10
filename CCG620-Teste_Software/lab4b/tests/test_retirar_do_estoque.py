from src.retirar_do_estoque import retirar_do_estoque
import pytest

def test_retirar_do_estoque():
    with pytest.raises (ValueError , match="Quantidade insuficiente em estoque"):
        retirar_do_estoque(0, 10)
