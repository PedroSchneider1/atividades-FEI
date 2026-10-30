

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_total_com_desconto__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_total_com_desconto__mutmut)
def total_com_desconto(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_orig(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_1(precos):
    total = None
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_2(precos):
    total = 1
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_3(precos):
    total = 0
    for i, preco in enumerate(None):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_4(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i > 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_5(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 4:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_6(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total = preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_7(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total -= preco * 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_8(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco / 0.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_9(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 1.9
        else:
            total += preco
    return round(total, 2)
def x_total_com_desconto__mutmut_10(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total = preco
    return round(total, 2)
def x_total_com_desconto__mutmut_11(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total -= preco
    return round(total, 2)
def x_total_com_desconto__mutmut_12(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(None, 2)
def x_total_com_desconto__mutmut_13(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, None)
def x_total_com_desconto__mutmut_14(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(2)
def x_total_com_desconto__mutmut_15(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, )
def x_total_com_desconto__mutmut_16(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 3)

mutants_x_total_com_desconto__mutmut['_mutmut_orig'] = x_total_com_desconto__mutmut_orig # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_1'] = x_total_com_desconto__mutmut_1 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_2'] = x_total_com_desconto__mutmut_2 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_3'] = x_total_com_desconto__mutmut_3 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_4'] = x_total_com_desconto__mutmut_4 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_5'] = x_total_com_desconto__mutmut_5 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_6'] = x_total_com_desconto__mutmut_6 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_7'] = x_total_com_desconto__mutmut_7 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_8'] = x_total_com_desconto__mutmut_8 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_9'] = x_total_com_desconto__mutmut_9 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_10'] = x_total_com_desconto__mutmut_10 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_11'] = x_total_com_desconto__mutmut_11 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_12'] = x_total_com_desconto__mutmut_12 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_13'] = x_total_com_desconto__mutmut_13 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_14'] = x_total_com_desconto__mutmut_14 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_15'] = x_total_com_desconto__mutmut_15 # type: ignore # mutmut generated
mutants_x_total_com_desconto__mutmut['x_total_com_desconto__mutmut_16'] = x_total_com_desconto__mutmut_16 # type: ignore # mutmut generated
