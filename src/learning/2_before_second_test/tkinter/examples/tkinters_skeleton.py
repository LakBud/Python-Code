print()
import tkinter as tk
from tkinter import font
from tkinter import ttk

# ---------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Skeleton_title_EXAMPLE")
root.geometry("200x200")

# ---------------------------------------------------------------------------------------------------------

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# ---------------------------------------------------------------------------------------------------------

style = ttk.Style()
themes = style.theme_names()
style.theme_use(themes[0]) # There exists 4 themes
style.configure(".", font=("Arial", 15))

# style.configure("classname.ELEMENT", font=("Arial", 15))

# ---------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------



root.mainloop()


# variable = ttk.ELEMENT(root)
# variable.grid(row=0, column=0, padx=5, pady=10, style="classname.ELEMENT")
# variable.pack(0, 0, padx=5, pady=10, style="classname.ELEMENT")

# Elements: Label, Button, Entry, ttk.Combobox, Spinbox, Radiobutton, StringVar(), Tk()
