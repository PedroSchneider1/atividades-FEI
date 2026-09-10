from src.classificar_estoque import classificar_estoque

def test_classificar_estoque() -> str:
    assert classificar_estoque(100) == "Alto"
    assert classificar_estoque(20) == "Normal"
