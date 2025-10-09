
# # ? You can decide functions with necessary valued parameters.
# def hello(name, age=0):
#     if age == 0:
#         print(f"Hello, {name}")
#     else:
#         print(f"Hello, {name} and you are {age} years old")
    
# username = str(input("Type your username: "))
# years = int(input("How old are you: "))

# # ! Here we are using the parameters when calling the function
# hello(username, years) 
# hello(years, username)
# hello(age=years, name=username) # ? You can force the order in the function by specifiying the function props

# def write_out_topic(*topic):
#     print(f"\nDatatype: {type(topic)}. Length: {len(topic)}")
    
#     if not topic:
#         print("I like: No topics")
#     else:
#         print(f"I like: ", end="")
#     for topics in topic:
#         print(f"{topics}, ", end="" )
#     print()
    
# write_out_topic()
# write_out_topic("IT", "Math")
# write_out_topic("History", "English", "IT")

# ! Example 2

# def f(x):
#     value = x**2 - 2*x + 1
#     return value # ? You can return a specific variable within the function to use

# print()
# for x_value in range(5):
#     print(f"({x_value}) = {f(x_value):>3}")

# ! Example 3

# def addition(a, b):
#     sum = a + b
#     return sum

# number1 = int(input("Type a whole number: "))
# number2 = int(input("Type another whole number: "))

# answer = addition(number1, number2)

# print(f"The sum of {number1} and {number2} = {answer}")

# ! Example 4
print()
def square_and_cube(number):
    return number**2, number**3

x_values = 1,3,6

for x in x_values:
    x_2, x_3 = square_and_cube(x)
    print(f"x = {x:2} | x^2 = {x_2:2} | x^3 = {x_3:2} ")

