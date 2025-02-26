import math as m
import tkinter as tk
from tkinter import messagebox

# 4 - Faça uma calculadora com as 4 operações básicas, potência, sen, cos,
# tan, log e raiz quadrada.
OPERATIONS = ['+', '-', 'x', '/', 'C', 'sen', 'cos', 'tan', 'log', '^', 'sqrt', '=']

n1 = 0
n2 = 0
operacao = ''

def criar_num(num):
    entrada.insert(tk.END, str(num))

def calculo(op):
    global n1, n2, operacao
    
    if op in OPERATIONS:
        if op == 'C':
            entrada.delete(0, tk.END)
            n1 = 0
            n2 = 0
            operacao = ''
        elif op == '=':
            if n1 != 0:
                if n2 == 0:
                    n2 = float(entrada.get())
                    entrada.delete(0, tk.END)
                    if operacao == '+':
                        resultado = n1 + n2
                    elif operacao == '-':
                        resultado = n1 - n2
                    elif operacao == 'x':
                        resultado = n1 * n2
                    elif operacao == '/':
                        if n2 != 0:
                            resultado = n1 / n2
                        else:
                            messagebox.showinfo("ERRO", "Divisão por zero!")
                            resultado = 'ERRO'
                    elif operacao == '^':
                        resultado = n1 ** n2
                    entrada.insert(tk.END, str(resultado))
                    n1 = resultado
                    n2 = 0
        elif op in ['+', '-', 'x', '/', '^']:
            n1 = float(entrada.get())
            entrada.delete(0, tk.END)
            operacao = op
        elif op == 'sen':
            seno = m.sin(m.radians(float(entrada.get())))
            entrada.delete(0, tk.END)
            entrada.insert(0, seno)
        elif op == 'cos':
            cos = m.cos(m.radians(float(entrada.get())))
            entrada.delete(0, tk.END)
            entrada.insert(0, cos)
        elif op == 'tan':
            tan = m.tan(m.radians(float(entrada.get())))
            entrada.delete(0, tk.END)
            entrada.insert(0, tan)
        elif op == 'log':
            log = m.log(float(entrada.get()), 10)
            entrada.delete(0, tk.END)
            entrada.insert(0, log)
        elif op == 'sqrt':
            sqrt = m.sqrt(float(entrada.get()))
            entrada.delete(0, tk.END)
            entrada.insert(0, sqrt)
        else:
            n1 = entrada.get()
    else:
        messagebox.showinfo("ERRO", "ERRO! Favor reiniciar o programa.")


# Window config
window = tk.Tk()
window.geometry('400x275')
window.title("Calculadora")
window.resizable(False, False)

window.grid_columnconfigure((0, 5), weight=1)

# Entry widget
entrada = tk.Entry()
entrada.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='ew')

# Buttons
b1 = tk.Button(window, text="1", width=2, command=lambda:criar_num(1))
b2 = tk.Button(window, text="2", width=2, command=lambda:criar_num(2))
b3 = tk.Button(window, text="3", width=2, command=lambda:criar_num(3))
b4 = tk.Button(window, text="4", width=2, command=lambda:criar_num(4))
b5 = tk.Button(window, text="5", width=2, command=lambda:criar_num(5))
b6 = tk.Button(window, text="6", width=2, command=lambda:criar_num(6))
b7 = tk.Button(window, text="7", width=2, command=lambda:criar_num(7))
b8 = tk.Button(window, text="8", width=2, command=lambda:criar_num(8))
b9 = tk.Button(window, text="9", width=2, command=lambda:criar_num(9))
b0 = tk.Button(window, text="0", width=6, command=lambda:criar_num(0))
b_equal = tk.Button(window, text="=", width=2, command=lambda: calculo('='))
b_sum = tk.Button(window, text="+", width=2, command=lambda: calculo('+'))
b_sub = tk.Button(window, text="-", width=2, command=lambda: calculo('-'))
b_multi = tk.Button(window, text="x", width=2, command=lambda: calculo('x'))
b_div = tk.Button(window, text="/", width=2, command=lambda: calculo('/'))
b_erase = tk.Button(window, text="C", width=8, command=lambda: calculo('C'))
b_sen = tk.Button(window, text="sen", width=2, command=lambda: calculo('sen'))
b_tan = tk.Button(window, text="tan", width=2, command=lambda: calculo('tan'))
b_cos = tk.Button(window, text="cos", width=2, command=lambda: calculo('cos'))
b_log = tk.Button(window, text="log", width=2, command=lambda: calculo('log'))
b_exp = tk.Button(window, text="^", width=2, command=lambda: calculo('^'))
b_sqrt = tk.Button(window, text="√", width=2, command=lambda: calculo('sqrt'))

# Buttons positions
b1.grid(row=3, column=0, padx=10, pady=10)
b2.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
b3.grid(row=3, column=2, padx=10, pady=10, sticky='ew')
b4.grid(row=2, column=0, padx=10, pady=10)
b5.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
b6.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
b7.grid(row=1, column=0, padx=10, pady=10)
b8.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
b9.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
b0.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='ew')
b_equal.grid(row=4, column=2, padx=10, pady=10, sticky='ew')
b_sum.grid(row=1, column=3, padx=10, pady=10, sticky='ew')
b_sub.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
b_multi.grid(row=3, column=3, padx=10, pady=10, sticky='ew')
b_div.grid(row=4, column=3, padx=10, pady=10, sticky='ew')
b_erase.grid(row=1, column=4, padx=10, pady=10, columnspan=2, sticky='ew')
b_sen.grid(row=2, column=4, padx=10, pady=10, sticky='ew')
b_tan.grid(row=3, column=4, padx=10, pady=10, sticky='ew')
b_cos.grid(row=2, column=5, padx=10, pady=10)
b_log.grid(row=3, column=5, padx=10, pady=10)
b_exp.grid(row=4, column=4, padx=10, pady=10, sticky='ew')
b_sqrt.grid(row=4, column=5, padx=10, pady=10)

window.mainloop()
# ===============================================================================
