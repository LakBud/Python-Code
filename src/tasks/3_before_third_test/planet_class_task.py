import math as m

print()
class Planet:
    """
    Docstring for Planet
    
    Class to create Planet objects
    """
    
    def __init__(self, name: str, diameter: float, distance_from_sun: float, total_moons: int = 0):
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :type name: str
        :param diameter: Description
        :type diameter: float
        :param distance_from_sun: Description
        :type distance_from_sun: float
        :param total_moons: Description
        :type total_moons: int
        
        Declares objects as the parameters
        """
        
        
        self.name = name
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.total_moons = total_moons
        
        
    def calculate_volume(self):
        
        """
        Docstring for calculate_volume
        
        Calculates the volume of the planet
        """
        
        radius = self.diameter / 2
        return round(4/3 * m.pi * radius**3, 2)
    
    def calculate_surface_area(self):
        
        """
        Docstring for calculate_surface_area
        
        :param self: Description
        """
        
        
        radius = self.diameter / 2
        return round(4 * m.pi * radius**2, 2)
    
    def show_info(self):
        
        """
        Docstring for show_info
        
        :param self: Description
        """
        
        print(f"{self.name:^25}|{self.diameter:^25}|{self.distance_from_sun:^25}|{self.total_moons:^25}|{round(self.calculate_volume(), 2):^25}|{round(self.calculate_surface_area(), 2):^25}|")

# Mercury = Planet("Mercury", 4879, 579.9)
# Venus = Planet("Venus", 12104, 108.21)
# Earth = Planet("Earth", 12742, 149.60, 1)
# Mars = Planet("Mars", 6779, 227.923, 2)
# Jupiter = Planet("Jupiter", 139822, 778.570, 2)
# Saturn = Planet("Saturn", 120536, 1433.530, 2)
# Uranus = Planet("Uranus", 50724, 2872.460, 2)
# Neptune = Planet("Neptune", 49244, 4495.06, 2)


# print(f"{"Planet":^25}|{"Diameter (km)":^25}|{"Sun Distance (million km)":^25}|{"Total Moons":^25}|{"Volume (km^3)":^25}|{"Surface Area (km^2)":^25}|")
# print("---" * 53)

# planet_list = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

# for planet in planet_list:
#     planet.show_info()


planets = {}

planets["Mercury"] = Planet("Mercury", 4879, 579.9)
planets["Venus"] = Planet("Venus", 12104, 108.21)
planets["Earth"] = Planet("Earth", 12742, 149.60, 1)
planets["Mars"] = Planet("Mars", 6779, 227.923, 2)
planets["Jupiter"] = Planet("Jupiter", 139822, 778.570, 2)
planets["Saturn"] = Planet("Saturn", 120536, 1433.530, 2)
planets["Uranus"] = Planet("Uranus", 50724, 2872.460, 2)
planets["Neptune"] = Planet("Neptune", 49244, 4495.06, 2)


try:
    choose_planet = str(input("Enter a planet in the solar system for details: "))
    
    for planet_key, planet_info in planets.items():
        if choose_planet == planet_key:
            print()
            print(f"{"Planet":^25}|{"Diameter (km)":^25}|{"Sun Distance (million km)":^25}|{"Total Moons":^25}|{"Volume (km^3)":^25}|{"Surface Area (km^2)":^25}|")
            print("---" * 53)
            planet_info.show_info()
            
except Exception as e:
    print(f"INVALID NAME!")
    print(f"System message: {e}")
    print()
    choose_planet = str(input("Enter a planet in the solar system for details: "))

