import tkinter as tk
from tkinter import font

def choose_car(event):
    chosen_car_index = car_listbox.curselection()[0]
    car_name = car_data[0][chosen_car_index]
    car_price = car_data[1][chosen_car_index]
    message.configure(text=f"You have chosen: {car_name} | The price is: {car_price} kr")

root = tk.Tk()
root.title("Listbox")
root.geometry("500x150")
 
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

car_data = [["Opel", "VW", "BMW", "Fiat", "Kia"], ["20000", "400000", "4050500", "1320230", "22390290" ]]


car_frame = tk.Frame(root)
car_frame.pack(pady=10) 


car_list_scroll = tk.Scrollbar(car_frame, orient="vertical")


car_listbox = tk.Listbox(car_frame, height=3, width=10, yscrollcommand=car_list_scroll.set)

for index, carlogo in enumerate(car_data[0]):
    car_listbox.insert(index, carlogo)


car_listbox.pack(side="left", fill="both")
car_list_scroll.configure(command=car_listbox.yview)
car_list_scroll.pack(side="right", fill="y")

car_listbox.bind("<<ListboxSelect>>", choose_car)


message = tk.Label(root, text="") 
message.pack(pady=5)

root.mainloop()
