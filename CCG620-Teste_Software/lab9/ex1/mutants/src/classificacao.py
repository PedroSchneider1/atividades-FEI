

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classificar_aluno__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_classificar_aluno__mutmut)
def classificar_aluno(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_orig(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_1(media, presenca):
    if media < 0 and media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_2(media, presenca):
    if media <= 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_3(media, presenca):
    if media < 1 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_4(media, presenca):
    if media < 0 or media >= 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_5(media, presenca):
    if media < 0 or media > 11:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_6(media, presenca):
    if media < 0 or media > 10:
        raise ValueError(None)
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_7(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("XXMedia invalidaXX")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_8(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_9(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("MEDIA INVALIDA")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_10(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 and presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_11(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca <= 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_12(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 1 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_13(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca >= 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_14(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 101:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_15(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError(None)
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_16(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("XXPresenca invalidaXX")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_17(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_18(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("PRESENCA INVALIDA")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_19(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca <= 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_20(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 76:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_21(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "XXReprovado por faltaXX"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_22(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_23(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "REPROVADO POR FALTA"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_24(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media > 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_25(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 8.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_26(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "XXAprovadoXX"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_27(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_28(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "APROVADO"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_29(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media > 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_30(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 6.0:
        return "Recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_31(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "XXRecuperacaoXX"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_32(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "recuperacao"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_33(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "RECUPERACAO"
    else:
        return "Reprovado"
def x_classificar_aluno__mutmut_34(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "XXReprovadoXX"
def x_classificar_aluno__mutmut_35(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "reprovado"
def x_classificar_aluno__mutmut_36(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "REPROVADO"

mutants_x_classificar_aluno__mutmut['_mutmut_orig'] = x_classificar_aluno__mutmut_orig # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_1'] = x_classificar_aluno__mutmut_1 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_2'] = x_classificar_aluno__mutmut_2 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_3'] = x_classificar_aluno__mutmut_3 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_4'] = x_classificar_aluno__mutmut_4 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_5'] = x_classificar_aluno__mutmut_5 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_6'] = x_classificar_aluno__mutmut_6 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_7'] = x_classificar_aluno__mutmut_7 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_8'] = x_classificar_aluno__mutmut_8 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_9'] = x_classificar_aluno__mutmut_9 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_10'] = x_classificar_aluno__mutmut_10 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_11'] = x_classificar_aluno__mutmut_11 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_12'] = x_classificar_aluno__mutmut_12 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_13'] = x_classificar_aluno__mutmut_13 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_14'] = x_classificar_aluno__mutmut_14 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_15'] = x_classificar_aluno__mutmut_15 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_16'] = x_classificar_aluno__mutmut_16 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_17'] = x_classificar_aluno__mutmut_17 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_18'] = x_classificar_aluno__mutmut_18 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_19'] = x_classificar_aluno__mutmut_19 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_20'] = x_classificar_aluno__mutmut_20 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_21'] = x_classificar_aluno__mutmut_21 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_22'] = x_classificar_aluno__mutmut_22 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_23'] = x_classificar_aluno__mutmut_23 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_24'] = x_classificar_aluno__mutmut_24 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_25'] = x_classificar_aluno__mutmut_25 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_26'] = x_classificar_aluno__mutmut_26 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_27'] = x_classificar_aluno__mutmut_27 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_28'] = x_classificar_aluno__mutmut_28 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_29'] = x_classificar_aluno__mutmut_29 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_30'] = x_classificar_aluno__mutmut_30 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_31'] = x_classificar_aluno__mutmut_31 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_32'] = x_classificar_aluno__mutmut_32 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_33'] = x_classificar_aluno__mutmut_33 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_34'] = x_classificar_aluno__mutmut_34 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_35'] = x_classificar_aluno__mutmut_35 # type: ignore # mutmut generated
mutants_x_classificar_aluno__mutmut['x_classificar_aluno__mutmut_36'] = x_classificar_aluno__mutmut_36 # type: ignore # mutmut generated
