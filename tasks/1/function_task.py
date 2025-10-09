
# 1
# def addition(a, b):
#     sum = a + b
#     return sum

# number1 = int(input("Type a whole number: "))
# number2 = int(input("Type another whole number: "))

# answer = addition(number1, number2)

# print(f"The sum of {number1} and {number2} = {answer}")

# 2
def listAfter10(list, limit=10):
    filtered_list = []
    for element in list:
        if element < limit:
            filtered_list.append(element)
    return filtered_list


list = [4,12,8,23,3,5,11,9]
new_list = listAfter10(list)

print()
print(f"Original list: {list}")
print(f"New list: {new_list}")
    
    

