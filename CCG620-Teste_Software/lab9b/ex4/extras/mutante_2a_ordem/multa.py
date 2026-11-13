# MUTANTE DE SEGUNDA ORDEM, aplicado a mao sobre ex4/src/multa.py
# Combina DOIS mutantes de primeira ordem que a suite BVA ja mata:
#   mutmut_10:  if dias <= 5   ->  if dias <= 6
#   mutmut_17:  0.01 * (dias - 5)  ->  0.01 * (dias - 6)
def valor_com_multa(valor, dias):
    if dias < 0 or dias > 60:
        raise ValueError("atraso invalido")
    if dias <= 6:                      # <-- mudanca 1 (era 5)
        multa = 0
    else:
        multa = 0.01 * (dias - 6)      # <-- mudanca 2 (era 5)
    total = valor * (1 + multa)
    return round(total, 2)
