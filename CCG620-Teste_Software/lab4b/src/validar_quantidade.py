def validar_quantidade(qtd: int) -> bool:
    if qtd >= 0 and qtd <= 1000:
        return True
    return False
