from frete import modalidade_frete


def test_correio_expresso():
    assert modalidade_frete(5, 300) == "Correio expresso"


def test_correio_economico():
    assert modalidade_frete(2, 1000) == "Correio economico"
