import tkinter as tk

# 1 - Interface gráfica para somar dois números:
def trocar_operacao():
    if botao_operacao["text"] == "+":
        botao_operacao["text"] = "-"
    else:
        botao_operacao["text"] = "+"


def resultado():
    n1 = float(entradaN1.get())
    n2 = float(entradaN2.get())
    if botao_operacao["text"] == "+":
        res = n1 + n2
    else:
        res = n1 - n2
    final.delete(0, tk.END)
    final.insert(0, res)


window = tk.Tk()

window.minsize(width=400, height=400)
window.title("Somar/Subtrair")

num1 = tk.Label(window, text="Digite o primeiro número: ", font=("Comic Sans", 14))
num2 = tk.Label(window, text="Digite o segundo número: ", font=("Comic Sans", 14))

num1.grid(row=0, column=0, padx=5, pady=5)
num2.grid(row=2, column=0, padx=5, pady=5)

entradaN1 = tk.Entry(window, width=20)
entradaN2 = tk.Entry(window, width=20)

entradaN1.grid(row=0, column=1, padx=5, pady=5)
entradaN2.grid(row=2, column=1, padx=5, pady=5)

botao_operacao = tk.Button(window, text="+", command=trocar_operacao)
botao_result = tk.Button(window, text="=", command=resultado)

botao_operacao.grid(row=1, column=3, padx=5, pady=5)
botao_result.grid(row=3, column=3, padx=5, pady=5)

resultado_final = tk.Label(window, text="Resultado: ", font=("Comic Sans", 14))
final = tk.Entry(window, width=20)

resultado_final.grid(row=4, column=0, padx=5, pady=5)
final.grid(row=4, column=1, padx=5, pady=5)


window.mainloop()

# ===============================================================================