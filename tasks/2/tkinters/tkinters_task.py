import tkinter as tk
from tkinter import font

# * 1

# def show_name():
#     name_out.configure(text=f"Hello: {name_in.get()}")

# root = tk.Tk()
# root.title("Hello Generator")

# frame = tk.Frame(root, padx=20, pady=29)
# frame.pack()

# name_in = tk.Entry(frame)
# name_in.grid(row=0, column=0, padx=5, pady=10)
# name_in.insert(0, "")

# button = tk.Button(frame, text="What is your Name", command=show_name)
# button.grid(row=1, column=0, padx=5, pady=10)

# name_out = tk.Label(frame)
# name_out.grid(row=2, column=0, padx=5, pady=10)

# root.mainloop()


# * 2


root = tk.Tk()
root.title("A Professional Calculator")

default_font = font.nametofont("TkDefaultFont")
default_font.config(family="Arial", size=29)

frame_text = tk.Frame(root, padx=10, pady=10)
frame_text.pack()

frame_operator = tk.Frame(root, padx=80, pady=20)
frame_operator.pack()


text_in1 = tk.Entry(frame_text, width=15, font="Arial 20")
text_in1.grid(row=0, column=0, padx=5, pady=10)
text_in1.insert(0, "")

text_in = tk.Entry(frame_text, width=15, font="Arial 20")
text_in.grid(row=0, column=1, padx=5, pady=10)
text_in.insert(0, "")


button_plus = tk.Button(frame_operator, text="+")
button_plus.grid(row=2, column=0)
button_minus = tk.Button(frame_operator, text="-")
button_minus.grid(row=2, column=1)
button_times = tk.Button(frame_operator, text="*")
button_times.grid(row=2, column=2)
button_divide = tk.Button(frame_operator, text="/")
button_divide.grid(row=2, column=3)



root.mainloop()
