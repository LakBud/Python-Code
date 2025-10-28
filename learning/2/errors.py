number_input = input("Write a Number: ")

try:
    number = float(number_input)
    rectangle = number**2
except:
    print("Have you wrote in a number?")
else:
    print(f"The rectangle of {number_input} is {rectangle}")
    


