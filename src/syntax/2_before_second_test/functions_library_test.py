# This is how to use files as librarys
from my_librarys import geometric_formulas as gf
print()

# ? from - takes a folder. 
# ? import - takes a file. 
# ? as - makes the file into a parameter

# 1)
# r = 2
# h = 4

# print(f"Surface of a cylinder is: {gf.surface_cylinder(radius=r, height=h)}")
# print(f"Surface of a cone is: {gf.surface_cone(radius=r, height=h)}")


# 2)

r = input("Write the radius: ")
print()

try:
    r_float = float(r)
    
except Exception as e:
    print(f"ERROR! Did you write a number?")
    print(f"Message from the system: {e}")
    
else:
    print(f"Surface of a cylinder is: {gf.surface_sphere(radius=r_float)}")
    print(f"Surface of a cylinder is: {gf.volume_sphere(radius=r_float)}")
