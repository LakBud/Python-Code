import tkinter as tk
from tkinter import font

def regn_ut():
    try:
        product = float(number1.get()) * float(number2.get())
        result.config(text=f"{product}")
    except ValueError:
        result.config(text="Error")

root = tk.Tk()
root.title("Task_2")

# Endre standard skrift (gjelder ikke input-widget'er)
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# Første tall
number1 = tk.Spinbox(root, width=5, from_=0, to=10, increment=1, font="Arial 20")
number1.grid(row=0, column=0, padx=5, pady=10)

# Multiplikasjonssymbol
symbol = tk.Label(root, width=2, text="*")
symbol.grid(row=0, column=1, padx=5, pady=10)

# Andre tall
number2 = tk.Spinbox(root, width=5, from_=0, to=10, increment=1, font="Arial 20")
number2.grid(row=0, column=2, padx=5, pady=10)

# "=" knapp
button = tk.Button(root, width=5, text="=", command=regn_ut)
button.grid(row=0, column=3, padx=5, pady=10)

# Resultat-label
result = tk.Label(root, width=10, text="", anchor="w")
result.grid(row=0, column=4, padx=5, pady=10)

# Kjør hovedløkken
root.mainloop()
