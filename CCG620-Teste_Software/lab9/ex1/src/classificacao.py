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
