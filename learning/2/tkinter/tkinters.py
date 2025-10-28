import tkinter as tk # A library built on Widgets (types) to create graphs
from tkinter import font # Fonts
print()

# -------------------------------------------------------------------------

# ? Root
# It has a type of module
print (type(tk))

root = tk.Tk()

# This has the type of tkinter.TK which is what we are going to use.
print(type(root)) 

# -------------------------------------------------------------------------

# ? Structure
# This is how to decide the title of the program
root.title("TKINTER TITLE")

# You can create frames which is meant to structure your elements. You can decide the element of this frame like padx or pady
frame = tk.Frame(root, padx=20, pady=20)

# This is how you print something out
frame.pack()   

# -------------------------------------------------------------------------

# ? Text Font

# nametofont() is used to set a default font
default_font = font.nametofont("TkDefaultFont") 

# configure() is used to change a elements properties
default_font.configure(family="Arial", size=29)

# -------------------------------------------------------------------------

# ? Text (with pack inside frame 1)

# Entry widget allows us to put stuff in the root or a frame
# For colors its bg for the background and fg for the text
text_in = tk.Entry(frame, bg="black", fg="white")

# Has a type of tkinter.Entry
print(type(text_in))

text_in.insert(0, "Write a text") # An example of how to change it
text_in.pack() # Pack() prints the non-/functional element

# -------------------------------------------------------------------------

# ? Second Frame for grid elements

frame2 = tk.Frame(root, padx=20, pady=20)
frame2.pack()

# ? Text with Grid inside frame2
text_in1 = tk.Entry(frame2, width=15, font="Arial 20")
text_in1.grid(row=0, column=0, padx=5, pady=10)
text_in1.insert(0, "Write a text again")

# -------------------------------------------------------------------------

# ? Button
button = tk.Button(frame, text="Show Text") # Exists text=, command=, etc
button.pack()

# -------------------------------------------------------------------------

# ? Label with colors
text_out = tk.Label(frame, bg="black", fg="white")
text_out.pack()

# -------------------------------------------------------------------------


# * Mainloop() shows the elements
root.mainloop()
