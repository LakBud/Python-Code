print()
number_list = [1,2,3,4,5,6,7,8,9,10]
word_list = ["Ha", "en", "veldig", "bra", "dag"]

print(f"number_list is of type: {type(number_list)}")
print(f"number_list is of length: {len(number_list)}") # ? len() = says the length to a list/array
print(f"word_list is of length: {len(word_list)}")

print("--------------------------------------------------")

print(f"the first element of number_list: {number_list[0]}") # list[index]
print(f"the third element of word_list: {word_list[2]}")

print("--------------------------------------------------")

print(f"Before change: {word_list}")
word_list[3] = "fantastisk"
print(f"After change: {word_list}")

print("--------------------------------------------------")

print(f"The last element in number_list: {number_list[len(number_list)-1]}")
print(f"The next last element in word_list: {word_list[len(word_list)-2]}")


print("--------------------------------------------------")

# list_variable = original_list[start : stop : steps]
alphabet_list = ["A", "B", "C", "D", "E", "F"]
print(alphabet_list[1:3])
print(alphabet_list[:2])
print(alphabet_list[2:])
print(alphabet_list[1::2])
print(alphabet_list[:])
print(alphabet_list[-1:-5:-1])


print("--------------------------------------------------")


# list.append(element) puts a element in the last of the list
# list.extend(elements or list) puts more elements
# list.insert(index, element) sets a element in a specific position in the list

alphabet_list = ["A", "B", "C"]

print(alphabet_list)

alphabet_list.append("D")
print(alphabet_list)

alphabet_list.extend(["F", "G", "H"])
print(alphabet_list)

alphabet_list.insert(4, "E")
print(alphabet_list)

print("--------------------------------------------------")


