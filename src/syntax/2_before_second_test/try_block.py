print()
# 1)

# number_input = input("Write a Number: ")

# try: # ? The block with the code executes with
#     number = float(number_input)
#     rectangle = number**2

# except Exception as e: # ! If an error returns, then it executes this and stores the error as an variable "e":
#     print("Have you wrote in a number?")
#     print(f"Message from the system: {e}") # ! Here it uses the variable with has the error message
    
# else: # ? If no exception is raised, it executes this:
#     print(f"The rectangle of {number_input} is {rectangle}")
    

# 2)


correct = False
rectangle = 0

while not correct:
    
    number_input = input("Write a number: ")
    
    try:
        number = float(number_input)
        rectangle = number**2
        correct = True
        
    except Exception as e:
        print(f"ERROR! Did you write a number?")
        print(f"Message from the system: {e}")
        

print(f"The rectangle of {number_input} is {rectangle}")