import tkinter as tk
from tkinter import font

def vis_result():
    result.configure(text=f"Number is: {number.get()}")

root = tk.Tk()

root.title("Spinboks-Example")


default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

number = tk.Spinbox(root, width=5, from_=0, to=10, increment=1, font="Arial 20")
number.grid(row = 0, column = 0, padx=5, pady=10)


button = tk.Button(root, width=10, text="Vis Tallet", command=vis_result)
button.grid(row = 0, column = 1, padx=5, pady=10)

result = tk.Label(root, width=25, bg="black", fg="white")
result.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()