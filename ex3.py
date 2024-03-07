linha = int(input("Digite a linha desejada: "))
coluna = input("Digite a coluna desejada: ")

if(linha % 2 == 0):
    if(coluna == "a"):
        print("Branco")
    elif(coluna == "c"):
        print("Branco")
    elif(coluna == "e"):
        print("Branco")
    elif(coluna == "g"):
        print("Branco")
    else:
        print("Preto")
else:
    if(coluna == "a"):
        print("Preto")
    elif(coluna == "c"):
        print("Preto")
    elif(coluna == "e"):
        print("Preto")
    elif(coluna == "g"):
        print("Preto")
    else:
        print("Branco")

