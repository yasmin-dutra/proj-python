# frontend.py
import tkinter as tk
from backend import add, subtract, multiply, divide

# Função para processar o cálculo
def process_calculation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        result_label.config(text=f"Resultado: {result}")
    except ValueError:
        result_label.config(text="Erro: Entrada inválida")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Campos de entrada
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Rótulos
label1 = tk.Label(root, text="Número 1:")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Número 2:")
label2.grid(row=1, column=0)

# Dropdown para operações
operation_var = tk.StringVar(root)
operation_var.set("+")  # valor padrão

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

# Botão de calcular
calculate_button = tk.Button(root, text="Calcular", command=process_calculation)
calculate_button.grid(row=3, column=1)

# Label para mostrar o resultado
result_label = tk.Label(root, text="Resultado:")
result_label.grid(row=4, column=1)

# Inicia o loop da interface
root.mainloop()