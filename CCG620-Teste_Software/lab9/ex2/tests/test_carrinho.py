from carrinho import total_com_desconto


# (a) Suíte inicial: assert fraco (só diz que o total é positivo)
#     -> 100% de ramos, mas MS = 4/16 = 25%
#
# (b) Mesmo assert trocado pelo valor exato, sem mudar a entrada:
#     10 + 20 + 30 + 40*0.9 + 50*0.9 = 141.0  -> 3 vivos (todos em round)
def test_total_exato():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0


# (d) Entrada que faltava: preço com centavos, cujo item com desconto gera
#     uma 3ª casa decimal.
#     10 + 20 + 30 + 10.51*0.9 = 69.459 -> round(.., 2) = 69.46
#     round(x, 3) daria 69.459  | round(x) / round(x, None) / round(x, ) dariam 69
def test_preco_com_centavos_exige_arredondamento_a_2_casas():
    assert total_com_desconto([10, 20, 30, 10.51]) == 69.46


# Extras de especificação (não eram necessários para o MS, mas documentam o contrato)
def test_tres_itens_nao_tem_desconto():
    assert total_com_desconto([10, 20, 30]) == 60


def test_lista_vazia_total_zero():
    assert total_com_desconto([]) == 0
