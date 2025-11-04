import tkinter as tk # A library built on Widgets (types) to create graphs
from tkinter import font # Fonts
print()


# -------------------------------------------------------------------------

# ? Root
root = tk.Tk()
root.title("TKINTER_2")


# -------------------------------------------------------------------------

# ? Spinbox = a select

number = tk.Spinbox(root, width=5, from_=0, to=10, increment=1)
number.grid(row=0, column=0, padx=5, pady=10)

# -------------------------------------------------------------------------


# ? Radio Select

def choose_answer():
    choice = choice_var.get()
    if choice != -1:
        if choice == 0:
            message.config(text="Are you sure?")
        else:
            message.config(text="That's good to hear!")

# A variable that stores the selected radio button value
choice_var = tk.IntVar(value=-1)

tk.Label(root, text="Do you exist?", width=10).grid(row=0, column=0, pady=2)

tk.Radiobutton(root, text="Yes", variable=choice_var, value=0, width=10, command=choose_answer).grid(row=1, column=0)
tk.Radiobutton(root, text="No", variable=choice_var, value=1, width=10, command=choose_answer).grid(row=1, column=1)

# Create the label first, then position it
message = tk.Label(root, width=20)
message.grid(row=1, column=2)




# -------------------------------------------------------------------------


# * Mainloop() shows the elements
root.mainloop()
