print()
import tkinter as tk
from tkinter import font



root = tk.Tk()
root.title("Tkinter_practice_task")
root.geometry("400x400")

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)


def choose_car_details():
    if not car_listbox.curselection():
        message.configure(text="Please select a car logo")
        return
    
    chosen_car_index = car_listbox.curselection()[0]
    selected_text = car_listbox.get(chosen_car_index)
    message.configure(text=f"Here are details about the {selected_text} cars:")
    
    details = ""
    
    for car in sorted_car_storage:
        if car["car_logo"] == selected_text:
            details += "-----------------------------------\n"
            for key, value in car.items():
                details += f"{key:^25}:{value:^20}\n"

    message_detail.configure(text=details)
        


# ---------------------------------------------------------------------------------------------------------

car_storage: list = [
                    {"car_logo": "BMW", "car_model": "M5", "km_state": 20423, "car_price": 439034},
                    {"car_logo": "BMW", "car_model": "M2", "km_state": 2323, "car_price": 23323},
                    
                    {"car_logo": "Mercedes", "car_model": "GLC", "km_state": 2232, "car_price": 23023},
                    {"car_logo": "Mercedes", "car_model": "GLA", "km_state": 29032, "car_price": 230932},
                    
                    {"car_logo": "Kia", "car_model": "Soul", "km_state": 328932, "car_price": 201209},
                    {"car_logo": "Kia", "car_model": "Sportage", "km_state": 9900, "car_price": 32023},
                    ]

car_id = lambda car_storage: car_storage["car_logo"]

sorted_car_storage: list = sorted(car_storage, key=car_id)

# ---------------------------------------------------------------------------------------------------------

car_frame = tk.Frame(root)
car_frame.pack(pady=20) 


car_list_scroll = tk.Scrollbar(car_frame, orient="vertical")
car_listbox = tk.Listbox(car_frame, height=5, width=15, yscrollcommand=car_list_scroll.set)

last_brand = None

for index, car in enumerate(sorted_car_storage):
    brand = car["car_logo"]
    if brand != last_brand:
        car_listbox.insert(index, car["car_logo"])
    last_brand = brand


car_listbox.pack(side="left", fill="both")
car_list_scroll.configure(command=car_listbox.yview)
car_list_scroll.pack(side="right", fill="y")

button = tk.Button(root, text="Show Info", command=choose_car_details)
button.pack()

message = tk.Label(root, text="") 
message.pack(pady=5)

message_detail_frame = tk.Frame(root)
message_detail_frame.pack(pady = 20)

message_detail = tk.Label(message_detail_frame, text="")
message_detail.pack()


root.mainloop()
