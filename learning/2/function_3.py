print()
from math import *

# 1) 
#

# Give clear and better names for functions + you can specify what values the params should be with a ": type"
# The same for the return with -> type: (after the () with the parameters)
# Specifying the type doesnt nothing to params or return.
# def surface_cylinder(radius: float, height: float) -> float:
#     surface = 2*pi*radius*(radius+height)
#     return round(surface,2)

# r = 2
# h = 4

# # Instead of just putting the variables, try to specify the params for better readability
# print(f"Surface-Areal to a Cylinder with the radius = {r} and the height = {h} is: {surface_cylinder(radius=r, height=h)}") 


# ---------------------------------------------------------------------------------------------------------


# ? Lambda-function
# The Lambda function is a short and anonymous function where you dont need to define it
# Returns a callable object

# ! Syntax: variable = lambda parameters: function
# Example: 
lambda_rectangle = lambda x: x*x

# ---------------------------------------------------------------------------------------------------------

# In sorted() you can specify the key and the reverse

# ? sorted(iterable, key=key, reverse=reverse)

# name_list = ["Karanveer", "Donny", "Sivert", "Johan", "Dina"]

# name_length = lambda name_list: len(name_list) # keys in sorted is usually len(element)

# sorted_name_list = sorted(name_list, key=name_length)
# print(sorted_name_list)

# ---------------------------------------------------------------------------------------------------------

# ? itemgetter()
# itemgetter() is a function from Python’s built-in operator module.
# It creates a callable (function-like object) that fetches items from its operand (like a list, tuple, or dictionary) using specified indices or keys.

from operator import itemgetter

alphabet_list = ["a", "b", "c", "d", "e"]

# Create a callable that gets the item at index 1
element_1 = itemgetter(1)

# Call it like a function with your list
element = element_1(alphabet_list)
print(element)  # Output: b

# Create a callable that gets the item at index 2
element_2 = itemgetter(2)

# Create a tuple with these callable functions
elements = element_1(alphabet_list), element_2(alphabet_list)
print(elements) # Output: ("b", "c")

# ---------------------------------------------------------------------------------------------------------

numbers = [1,2,3,4,5,56,7,20,7,98]

# ? max() = a function which returns the biggest value in a dictionary or list

print(max(numbers)) # 98

# ? min() = a function which returns the smallest value in a dictionary or list

print(min(numbers)) # 1