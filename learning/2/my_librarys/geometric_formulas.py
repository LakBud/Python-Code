from math import *

def area_trapes(side1: float, side2: float, height: float) -> float:
    area = ((side1 + side2)*height)/2
    return round(area)

def area_sirkel(radius: float) -> float:
    area = pi*radius**2
    return round(area)

def surface_cylinder(radius :float, height :float) -> float:
    surface = 2*pi*radius*(radius+height)
    return round(surface,2)

def volume_cylinder(radius :float, height :float) -> float:
    volume = pi*radius**2*height
    return round(volume,2)
    
def surface_cone(radius :float, height :float) -> float:
    side = sqrt(radius**2 + height**2)
    surface = pi*radius*(radius + side)
    return round(surface,2)

def volume_cone(radius :float, height :float) -> float:
    volume = pi*radius**2*height/3
    return round(volume,2)
    
def area_trapezoid(side1: float, side2: float, height: float) -> float:
    area = ((side1 + side2)*height)/2
    return round(area)


def surface_sphere(radius: float) -> float:
    surface = 4*pi*radius**2
    return round(surface, 2)

def volume_sphere(radius: float) -> float:
    volume = (4/3)*pi*radius**3
    return round(volume, 2)

