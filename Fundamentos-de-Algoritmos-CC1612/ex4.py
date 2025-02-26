lados = int(input())
if(lados > 10):
    print("Erro!")
elif(lados >= 3):
    if(lados == 3):
        print("triângulo")
    if(lados == 4):
        print("quadrilátero")
    if(lados == 5):
        print("pentágono")        
    if(lados == 6):
        print("hexágono")
    if(lados == 7):
        print("heptágono")
    if(lados == 8):
        print("octógono")
    if(lados == 9):
        print("eneágono")
    if(lados == 10):
        print("decágono")
else:
    print("Erro!")