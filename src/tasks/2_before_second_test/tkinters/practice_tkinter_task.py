print()
import json
import tkinter as tk
from tkinter import font



root = tk.Tk()
root.title("Tkinter_practice_task")
root.geometry("400x600")

default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# ---------------------------------------------------------------------------------------------------------

cars: str = "data/car_register.json"

with open(cars, encoding="utf-8") as car_storage:
    car_data: list = json.load(car_storage)


car_id: str = lambda car: car["brand"]
sorted_car_storage: list = sorted(car_data, key=car_id)


# ---------------------------------------------------------------------------------------------------------


def choose_car_details():
    if not car_listbox.curselection():
        message.configure(text="Please select a car logo")
        return
    
    chosen_car = car_listbox.curselection()
    selected_text = car_listbox.get(chosen_car)
    message.configure(text=f"Here are details about the {selected_text} cars:")
    
    details_content = ""
    
    for car in sorted_car_storage:
        if car["brand"] == selected_text:
            for details in car["details"]:
                details_content += "\n"
                for key, value in details.items():
                    details_content += f"{key:^25}{value:^25}\n"


    message_detail.configure(text=details_content)




# ---------------------------------------------------------------------------------------------------------

car_frame = tk.Frame(root)
car_frame.pack(pady=20) 


car_list_scroll = tk.Scrollbar(car_frame, orient="vertical")
car_listbox = tk.Listbox(car_frame, height=5, width=15, yscrollcommand=car_list_scroll.set)


for index, car in enumerate(sorted_car_storage):
    car_listbox.insert(index, car["brand"])



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
