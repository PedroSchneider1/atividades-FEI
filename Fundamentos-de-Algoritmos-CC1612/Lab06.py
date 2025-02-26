from math import sqrt
"""def hipotenusa(a,b):
    return sqrt(a**2 + b**2)

a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))

h = hipotenusa(a,b)
print(f"Hipotenusa: {h:.2f}")"""

"""def calcPeso(planeta, peso):
    if(planeta == "Mercúrio"):
        return peso*0.37
    elif(planeta == "Vênus"):
        return peso*0.88
    elif(planeta == "Marte"):
        return peso*0.38
    elif(planeta == "Júpiter"):
        return peso*2.64
    elif(planeta == "Saturno"):
        return peso*1.15
    elif(planeta == "Urano"):
        return peso*1.17
    else:
        return peso*1.18

planeta = input("Digite o o nome do planeta desejado: ")
peso = float(input("Digite o peso da pessoa na Terra em kg: "))
pesoFinal = calcPeso(planeta, peso)

print(f"Peso em {planeta}: {pesoFinal:.2f}")"""

"""def test_prime(num):
    if num <= 1:  # Nao é primo
        return False
    elif num == 2:  # É primo
        return True

    eh_primo = True
    # Se não for possível dividir o número por nenhum número entre 2 e a raiz quadrada do número, então ele é primo

    raiz = int(sqrt(num)) + 1
    for j in range(2, raiz):
        if num % j == 0:
            eh_primo = False
            break
    return eh_primo

print(test_prime(8))"""

"""
#Solução pelo Copilot
def produtorio(*args):
    
    #Calcula o produtório dos valores passados como argumentos.

    #Args:
        #*args: Valores para os quais o produtório será calculado (entre 3 e 6 valores).

    #Returns:
        #float: O resultado do produtório.
    
    if len(args) < 3 or len(args) > 6:
        raise ValueError("A função deve receber entre 3 e 6 parâmetros.")

    resultado = 1
    for valor in args:
        resultado *= valor

    return resultado"""

"""def produtorio(n1,n2,n3,n4=1,n5=1,n6=1):

    resultado = n1*n2*n3*n4*n5*n6

    return resultado"""

def tarifa(km):
    tarifa = 10 + 4*km #R$10 + R$0,50 por 125m percorridos
    return tarifa

dist = int(input("Digite a quantidade de quilômetros: "))
tarifaFinal = tarifa(dist)

print(f"Tarifa {tarifaFinal:.2f}")