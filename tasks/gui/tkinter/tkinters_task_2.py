import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Task_2")
root.geometry("800x500")


# Endre standard skrift (gjelder ikke input-widget'er)
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)


# ---------------------------------------------------------------------------------------------------------------


choice_var = tk.IntVar(value=0)
operator_symbol = tk.StringVar(value="")

def update_operator():
    choice = choice_var.get()
    symbols = ["+", "-", "*", "/"]
    operator_symbol.set(symbols[choice])


def calculate():
    choice = choice_var.get()

    try:
        n1 = float(number1.get())
        n2 = float(number2.get())
        
        if choice == 0:
            product = n1 + n2
            operator_symbol.set("+")
    
        elif choice == 1:
            product = n1 - n2
            operator_symbol.set("-")
            
        elif choice == 2:
            product = n1 * n2
            operator_symbol.set("*")
            
        elif choice == 3:
            
            if n2 == 0:
                result.config(text="Error")
                return error_message.config(text="Cannot divide by zero")
    
            product = n1 / n2
            operator_symbol.set("/")
            
        else:
            error_message.config(text="")
        
    except ValueError as e:
        result.config(text="Error")
        error_message.config(text=str(e))
        
    else:
        result.config(text=f"{product}")
            
            

# ---------------------------------------------------------------------------------------------------------------

calculator_frame = tk.Frame(root)
calculator_frame.grid()

# First number
number1 = tk.Spinbox(calculator_frame, width=5, from_=0, to=10, increment=1, font="Arial 20")
number1.grid(row=0, column=0, padx=5, pady=10)

# Symbol
symbol = tk.Label(calculator_frame, width=2, textvariable=operator_symbol)
symbol.grid(row=0, column=1, padx=5, pady=10)


# Second Number
number2 = tk.Spinbox(calculator_frame, width=5, from_=0, to=10, increment=1, font="Arial 20")
number2.grid(row=0, column=2, padx=5, pady=10)

# "=" Button
button = tk.Button(calculator_frame, width=5, text="=", command=calculate)
button.grid(row=0, column=3, padx=5, pady=10)


# Result-label
result = tk.Label(calculator_frame, width=10, text="", anchor="w")
result.grid(row=0, column=4, padx=5, pady=10)


# ---------------------------------------------------------------------------------------------------------------

button_frame = tk.Frame(root)
button_frame.grid()

# Radio Selects
tk.Radiobutton(button_frame, text="Addition (+)", variable=choice_var, value=0, command=update_operator).grid(row=2, column=0)
tk.Radiobutton(button_frame, text="Subtraction (-)", variable=choice_var, value=1, command=update_operator).grid(row=2, column=1)
tk.Radiobutton(button_frame, text="Multiplication (*)", variable=choice_var, value=2, command=update_operator).grid(row=2, column=2)
tk.Radiobutton(button_frame, text="Division (/)", variable=choice_var, value=3, command=update_operator).grid(row=2, column=3)

update_operator()

# ---------------------------------------------------------------------------------------------------------------

error_frame = tk.Frame(root)
error_frame.grid()

error_message = tk.Label(error_frame, width=20, text="", anchor="w", fg="red")
error_message.grid(row=8, column=3, pady=3, padx=5)

# ---------------------------------------------------------------------------------------------------------------

# Run the Program
root.mainloop()
