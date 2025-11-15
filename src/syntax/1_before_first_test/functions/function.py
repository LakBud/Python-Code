print()
# list = []
# counter = 0

# while True:
#     list.append(counter)
    
#     if counter > 9:
#         break

#     counter += 1

# print(list) 

# list = []
# for i in range(1,11):
    
#     if i % 2 != 0:
#         continue
    
#     list.append(i)
    
# print(list)

print("This program lets you create a list with integers")
print("When you are done, click ENTER without writing anything")

total_numbers = 0
number_list = []

while True:
  texts = input("Write an integer: ")
  
  if texts == "":
    break
      
  if texts.isnumeric():
    tall = int(texts)
    number_list.append(tall)
    total_numbers +=1
    print(f"You wrote the integer: {tall}\n")
    
  else:
    print(f"{texts} is not a integer\n")
    
print(f"\nYou have written {total_numbers} integers")
print(f"This is your integer list: {number_list}")