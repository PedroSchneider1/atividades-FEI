from src.validar_quantidade import validar_quantidade

def test_validar_quantidade():
    assert validar_quantidade(0) == True
    assert validar_quantidade(1000) == True
