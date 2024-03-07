animal = (input("Primeira palavra: "))

if(animal == "invertebrado"):
    categoriaAnimal = (input("Segunda palavra: "))
    if(categoriaAnimal == "inseto"):
        habitoAlimentar = (input("Terceira palavra: "))
        if(habitoAlimentar == "hematofago"):
            print("pulga")
        else:
            print("lagarta")    
    else:
        categoriaAnimal = (input("Terceira palavra: "))
        if(categoriaAnimal == "hematofago"):
            print("sanguessuga")
        else:
            print("minhoca")

else:
    categoriaAnimal = (input("Segunda palavra: "))
    if(categoriaAnimal == "mamifero"):
        habitoAlimentar = (input("Terceira palavra: "))
        if(habitoAlimentar == "herbivoro"):
            print("vaca")
        else:
            print("homem")
    else:
        habitoAlimentar = (input("Terceira palavra: "))
        if(habitoAlimentar == "carnivoro"):
            print("aguia")
        else:
            print("pomba")