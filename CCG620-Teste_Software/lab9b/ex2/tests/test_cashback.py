from cashback import cashback


def test_cashback_valor_exato():
    # 50 nao entra (< 100); 100 -> 5.0; 200 -> 10.0; total = 15.0
    # Mata 7 dos 10 vivos da suite inicial (revelacao: assert exato)
    assert cashback([50, 100, 200]) == 15.0


def test_cashback_exige_arredondamento_em_duas_casas():
    # 111.11 * 0.05 = 5.5555  (4 casas decimais!)
    #   round(t, 2)    -> 5.56   (correto)
    #   round(t, 3)    -> 5.556  (mutmut_13 morre)
    #   round(t)       -> 6      (mutmut_10 e mutmut_12 morrem)
    # Esta entrada PRECISA de um resultado com mais de 2 casas decimais
    # e nao inteiro, senao o round() nao "infecta" o estado do programa.
    assert cashback([111.11]) == 5.56


def test_limite_exato_100_recebe_cashback():
    # documenta a fronteira >= 100 (ja morta pela lista do 1o teste)
    assert cashback([100]) == 5.0


def test_logo_abaixo_do_limite_nao_recebe():
    assert cashback([99.99]) == 0


def test_lista_vazia():
    assert cashback([]) == 0
