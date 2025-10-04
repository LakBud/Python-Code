print()
# ? word_list = ["Have", "a", "good", "day"] 
# ? number_list = [1,2,3,4,5]
# ? empty_list = []
# ? boolean_list = [True, False, True, False]

# * list_with_list_number = [[1,2,3], [3,4,5], [6,7,8]]
# * list_with_list_word = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

# list = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

# for row in list:
#     for word in row:
#         print(f"{word:>2}", end="") # end = hva slutten skal bli
#     print()
    

# for i in range(0,len(list)):
#     for j in range(0,len(list[i])):
#         print(f"{list[i][j]:>3},", end="")
#     print()


# List Comprehension

# x = [x for x in range(1, 11)]
# print(x)
# square_list = [x**2 for x in range(1,11)]
# print(square_list)
# square_odd_list = [x**2 for x in range(1,11) if x**2 % 2 == 0]
# print(square_odd_list)


number = [1,2,3,3,3,4,3,3,5,3,3,6,3] 

# ! Aldri bruk for løkke for å endre elementer
for n in number:
    if n == 3:
     number.remove(n)
    
print(number)

# * Bruk en while løkke istedenfor
while 3 in number:
    number.remove(3)
print(number)