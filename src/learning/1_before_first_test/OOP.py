# 1) Type
# Number = 12
# text = "Hello"
# list = [1,2,3]

# def function(x):
#     return x

# print(f"variabelen Number er av type {type(Number)}")
# print(f"variabelen text er av type {type(text)}")
# print(f"variabelen list er av type {type(list)}")
# print(f"function er av type {type(function)}")

# 2) Classes

# class Person: # ? Generates a class
#     first_name = "N"
#     last_name = "N"
    
    
# person = Person() # ? Creates a object of the class Person
# person.last_name = "Khan"

# print(f"Variabelen person er av type {type(person)}")
# print(f"first_name: {person.first_name}. last_name: {person.last_name}")

# 3) Letter-changing
text = input("Write something: ")

print(f"Only big letters: {text.upper()}")
print(f"Only small letters: {text.lower()}")
print(f"Only the first letter gets big: {text.title()}")
print(f"There is {text.count("e")} of the letter e in the text")
