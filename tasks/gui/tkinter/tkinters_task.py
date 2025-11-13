import tkinter as tk
from tkinter import font


def show_name():
    name_out.configure(text=f"Hello: {name_in.get()}")

root = tk.Tk()
root.title("Hello Generator")

frame = tk.Frame(root, padx=20, pady=29)
frame.pack()

name_in = tk.Entry(frame)
name_in.grid(row=0, column=0, padx=5, pady=10)
name_in.insert(0, "")

button = tk.Button(frame, text="What is your Name", command=show_name)
button.grid(row=1, column=0, padx=5, pady=10)

name_out = tk.Label(frame)
name_out.grid(row=2, column=0, padx=5, pady=10)

root.mainloop()

