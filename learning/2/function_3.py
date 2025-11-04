print()
from math import *

# 1) 
#

# Give clear and better names for functions + you can specify what values the params should be with a ": type"
# The same for the return with -> type: (after the () with the parameters)
# Specifying the type doesnt nothing to params or return.
def surface_cylinder(radius: float, height: float) -> float:
    surface = 2*pi*radius*(radius+height)
    return round(surface,2)

r = 2
h = 4

# Instead of just putting the variables, try to specify the params for better readability
print(f"Surface-Areal to a Cylinder with the radius = {r} and the height = {h} is: {surface_cylinder(radius=r, height=h)}") 