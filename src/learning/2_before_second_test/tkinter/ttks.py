print()
import tkinter as tk
from tkinter import font
from tkinter import ttk

# ---------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("TTK")
root.geometry("200x200")

def combobox_choice(event):
    print(f"Chosen: {combo_box.get()}")

# ---------------------------------------------------------------------------------------------------------

style = ttk.Style() # The Variable which stores the style variable
themes = style.theme_names() # Stores a variable to the exisitng themes
style.theme_use(themes[3]) # .theme_use() is how you use a existing theme

style.configure(".", font=("Arial", 15)) # Here you can configure all elements styling.

# Here you configure selected Tkinter buttons styling with the class Red_button
style.configure("Red_button.TButton", font=("Arial", 20, "bold"), background="red") 

# ---------------------------------------------------------------------------------------------------------

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# ---------------------------------------------------------------------------------------------------------

label = ttk.Label(root, width=20, text="This is a TKINTER label").grid(row=0, column=0)

entry = ttk.Entry(root).grid(row=2, column=0)

button = ttk.Button(root, text="Click me").grid(row=3, column=0)
button2 = ttk.Button(root, text="Clicky me", style="Red_button.TButton").grid(row=5, column=0)

# ---------------------------------------------------------------------------------------------------------
# Dropdown GUI

car_list = ["Opel", "VW", "BMW", "Fiat"]
combo_choice = tk.StringVar()

# With ttk you can create dropdowns with ttk.Combobox()
combo_box = ttk.Combobox(root, textvariable=combo_choice, values=car_list)
combo_box.set(car_list[0])
combo_box.grid(row=8, column=0)
combo_box.bind("<<ComboboxSelected>>", combobox_choice)

# ---------------------------------------------------------------------------------------------------------

root.mainloop()
