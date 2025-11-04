import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Calculator_task")

default_font = font.nametofont("TkDefaultFont")
default_font.config(family="Arial", size=20)

# Første tall
number1 = tk.Spinbox(root, width=5, from_=0, to=10, increment=1, font="Arial 20")
number1.grid(row=0, column=0, padx=5, pady=10)


root.mainloop()