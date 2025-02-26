faixaEtaria = input("Digite a faixa etária: ")
if(faixaEtaria == "Bebê"):
    print("menor que 2 anos")
elif(faixaEtaria == "Criança"):
    print("de 3 a 10 anos")
elif(faixaEtaria == "Adolescente"):
    print("de 11 a 17 anos")
elif(faixaEtaria == "Adulto"):
    print("de 18 a 64 anos")
else:
    print("maior que 65 anos")