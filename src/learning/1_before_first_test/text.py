
# * 1.

name = "Buddo"
age = 25

# ? ? 1)
print("Hi, my name is", name, "and i am", age, "years old")

# ? 2)
print("Hi, my name is " + name + " and i am " + str(age) + " years old")


# ? 3)
print("Hi, my name is %s and i am %s years old" %(name, age))

# ? 4)
print("Hi, my name is {} and i am {} years old" .format(name, age))

# ? 5)
print(f"Hi, my name is {name} and i am {age} years old")


# ----------------------------------------------------------------------------------------------------

print("Text in a line. \nText in the next line") # \n = space
print()
print("Text in a line. \n\nText in the next line") # \n\n = two spaces

print("-------------------")

tall = input("Write a whole number: ")

if tall.isnumeric(): # You can check if an input value is a whole number with isnumeric()
    print("So good that you wrote an integer")
else: 
    print("That you wrote was not an integer")

