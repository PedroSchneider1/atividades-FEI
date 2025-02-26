"""Faça um programa que leia uma a um modelos de cinco carros (exemplos: FUSCA, GOL, VECTRA etc) e os guarde em uma mesma lista.
Leia (um a um) uma outra lista  com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.
Calcule e mostre:
- O modelo do carro mais econômico;
- Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros."""
"""carros = []
consumo = []
economico = 0
indexEco = 0

for i in range(5):
    carros.append(input())

for i in range(5):
    consumo.append(int(input()))
    if consumo[i] > economico:
        economico = consumo[i]
        indexEco = i

print(carros[indexEco])

for i in range(len(consumo)):
    print(f"{1000/consumo[i]:.0f}")"""

###

"""Faça um programa que calcule a média e o desvio padrão de um vetor com os valores
e o número de elementos definido pelo usuário."""
"""from math import pow, sqrt

x = []
somaDesvioX = 0
somaMediaX = 0
mediaX = 0

n = int(input("Qual o tamanho da lista: "))
print("Digite os valores: ")

for i in range(n):
    x.append(int(input()))
    somaMediaX += x[i]

mediaX = somaMediaX/n

for i in range(n):
    somaDesvioX += pow((x[i]-mediaX),2)

desvio = sqrt(somaDesvioX/n)

print(f"Média = {mediaX:.2f} e Desvio = {desvio:.4f}")"""

###

"""Crie um programa que leia números inteiros do usuário até que o número 0 seja inserido. 
Uma vez que todos os números inteiros tenham sido lidos, seu programa deve exibir todos os números negativos,
seguidos por todos os números positivos.
Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram inseridos pelo usuário"""
"""pos = []
neg = []
num = int(input())

while(num != 0):
    if(num > 0):
        pos.append(num)
    else:
        neg.append(num)
    num = int(input())

print(str(neg)[1:-1]) # Remove os colchetes na hora de imprimir a lista
print(str(pos)[1:-1])"""

###

"""Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. 
Armazene os números pares na lista par e os números ímpares na lista impar. 
Imprima as três listas no final."""
"""par = []
impar = []
numeros = []

for i in range(20):
    num = int(input())
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

for i in range(len(numeros)):
    print(f"{numeros[i]}", end=" ")

print()

for i in range(len(impar)):
    print(f"{impar[i]}", end=" ")

print()

for i in range(len(par)):
    print(f"{par[i]}", end=" ")"""

###

"""Faça um programa que leia cada componente de vetores de tamanho três a serem multiplicados
e apresente como resultado o resultado escalar."""
"""vetorA = []
vetorB = []

print("Digite o vetor 1:")

for i in range(3):
    vetorA.append(int(input()))

print("Digite o vetor 2:")

for i in range(3):
    vetorB.append(int(input()))

escalar = 0

for i in range(3):
    escalar += vetorA[i]*vetorB[i]

print(escalar)"""

###

"""Escreva uma função que recebe uma lista de números inteiros e
retorne uma nova lista que contém o quadrado de cada um desses números.
Você só precisa entregar o código da função."""
from math import pow

def quadrado(num):

    for i in range(len(num)):
        num[i] = pow(num[i], 2)

    return num

print(quadrado([1, 2, 3, 4, 5, 6, 7]))