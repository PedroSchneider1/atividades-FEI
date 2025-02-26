import tkinter as tk
from tkinter import messagebox

# 3 - Crie um programa que lê uma letra do alfabeto por uma caixa de texto. Se
# o usuário digitar a, e, i, o ou u, seu programa deverá exibir uma mensagem
# indicando que a letra inserida é uma vogal (utilize caixas de mensagem -
# messagebox). Se o usuário digitar y, seu programa deve exibir uma
# mensagem indicando que às vezes y é uma vogal (depende da língua, no
# inglês, por exemplo), e às vezes y é uma consoante. Caso contrário, seu
# programa deve exibir uma mensagem indicando que o letra é uma
# consoante

VOWELS = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

def verificar():
    if entrada.get() in VOWELS:
        messagebox.showinfo("Vogal!", "É uma vogal!")
    elif entrada.get() == 'y' or entrada.get() == 'Y':
        messagebox.showinfo("Vogal/Consoante!", "É uma vogal em alguns idiomas, mas em outros não!")
    else:
        messagebox.showinfo("Consoante!", "É uma consoante!")


window = tk.Tk()
window.minsize(width=400, height=100)
window.geometry('400x100')
window.title("Vogal ou consoante?")

rotulo = tk.Label(window, text="Digite uma letra: ", font=("Comic Sans", 14))
rotulo.grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(window, width=20)
entrada.grid(row=0, column=1, padx=5, pady=5)

verify = tk.Button(window, text="Verificar", command=verificar)
verify.grid(row=1, column=0, padx=5, pady=5)


window.mainloop()
# ===============================================================================