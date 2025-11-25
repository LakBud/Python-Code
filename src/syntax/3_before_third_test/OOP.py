print()
# # ? This is a class which describes attributes to parameters
# class Person:
    
#     # ? This is a constructor which purpose is to initialize/create the objects attributes or state.
#     # ! The constructor functions name is always __init__ which never returns anything
    
#     def __init__(self, first_name, last_name, age):
#         # ? The first parameter within the constructor has to be self which represents the class itself and its supposed params
#         # * Used here to refer to the users parameters

#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person("Jimmy", "Devold", 15) # * Here the class is defined with Jimmy as first_name, Devold as last_name, 15 as age.
# p2 = Person("Max", "Timmy", 20)

# age_sum = p1.age + p2.age # ? You can take objects from the class by using class.object

# print(age_sum)

"""
This is a doc string which starts and ends with ("" ")
"""

class Person:
    
    """
    Class to create Person-objects
    
    Parameters:
        name (str): persons name
        country (str): persons country
    """
    
    
    def __init__(self, name: str, country: str = "Norway") -> None: # ? You can give value to default parameters which can be overriden
        """
        Constructor for class
        """
        self.name = name
        self.country = country

Norwegian = Person("Ola Nordmann")
Swedish = Person("Svante Sturesson", "Sweden")

print(f"{Norwegian.name} lives in {Norwegian.country}")
print(f"{Swedish.name} lives in {Swedish.country}")