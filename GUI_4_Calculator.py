import math as m
import tkinter as tk

# 4 - Faça uma calculadora com as 4 operações básicas, potência, sen, cos,
# tan, log e raiz quadrada.
OPERATIONS = ['+', '-', 'x', '/', 'C', 'sen', 'cos', 'tan', 'log', '^', 'sqrt', '=']

def criar_num(num):
    entrada.insert(0, str(num))

def calculo(op):
    n1 = ''
    if op in OPERATIONS:
        entrada.delete(0, tk.END)
        print("cu")
    else:
        print(n1)


window = tk.Tk()
window.geometry('275x275')
window.title("Calculadora")
window.resizable(False, False)

window.grid_columnconfigure((0, 5), weight=1)

entrada = tk.Entry()
entrada.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='ew')

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