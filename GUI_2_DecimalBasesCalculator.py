import tkinter as tk

# 2- Faça uma calculadora para transformar números decimais em: binários,
# hexadecimais ou octais. Cada base numérica deve ter um botão para
# realizar a conversão

def converter(n):
    try:
        num = int(entrada.get())
        if n == 1:
            final.delete(0, tk.END)
            final.insert(0, bin(num))
        elif n == 2:
            final.delete(0, tk.END)
            final.insert(0, hex(num))
        elif n == 3:
            final.delete(0, tk.END)
            final.insert(0, oct(num))
        else:
            final.delete(0, tk.END)
            final.insert(0, "ERRO")
    except ValueError:
        final.delete(0, tk.END)
        final.insert(0, "Entrada inválida")

window = tk.Tk()
window.minsize(width=400, height=400)
window.title("Mudança de bases")

rotulo = tk.Label(window, text="Número decimal:", font=("Comic Sans", 14))
rotulo.pack(padx=5, pady=5)

entrada = tk.Entry(window, width=20)
entrada.pack(padx=5, pady=5)

botao_binario = tk.Button(window, text="Binário", command=lambda: converter(1))
botao_hexa = tk.Button(window, text="Hexadecimal", command=lambda: converter(2))
botao_octal = tk.Button(window, text="Octal", command=lambda: converter(3))

botao_binario.pack(padx=5, pady=5)
botao_hexa.pack(padx=5, pady=5)
botao_octal.pack(padx=5, pady=5)

final = tk.Entry(window, width=20)
final.pack(padx=5, pady=5)

window.mainloop()
# ===============================================================================