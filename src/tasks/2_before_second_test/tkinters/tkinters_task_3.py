import tkinter as tk
from tkinter import font

# ---------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Cars")
root.geometry("200x200")

# ---------------------------------------------------------------------------------------------------------

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# ---------------------------------------------------------------------------------------------------------

car_list = ["Opel", "BMW", "VW", "Fiat"]


tk.Label(root, width=10, text="Choose car") \
    .grid(row=0, column=0, padx=5, pady=5)

car_index_var = tk.IntVar(value=-1)

def choose_car():
    car_index = car_index_var.get()
    if car_index != -1:
        car_logo = car_list[car_index]
        message.configure(text=f"You chose: {car_logo}")
        
        


for index, carlogo in enumerate(car_list):
    tk.Radiobutton(root, text=carlogo, variable=car_index_var, value=index, command=choose_car) \
        .grid(row=index + 1, column=0, padx=10)




message = tk.Label(root) 
message.grid(row=len(car_list)+2, column=0, padx=5, pady=5)

root.mainloop()
