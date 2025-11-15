print()
number_list = [1,2,3,4,5,6,7,8,9,10]
word_list = ["Ha", "en", "veldig", "bra", "dag"]

print("--------------------------------------------------")

word_list.remove("bra")
print(word_list)

del word_list[4:]
print(word_list)

deleted_element = word_list.pop(0)
print(f"deleted_element: {deleted_element}")
print(word_list)

print("--------------------------------------------------")

# liste.index(element): Finds and returns the index to the first element which exists in the list. If there doesnt exist, an error will occur.
# liste.index(element: index): Does the same, but starts from an decided index.
# element in liste: Checks if an element exists within the list (can be used in while-loops / if-sentences)
# liste.count(element): Returns total count of the element within a list

list = ["A", "B", "C", "D", "C", "B", "A"]
word = "A"
print(f"The first attempt in \"{word}\" is in index: {list.index(word)}")
print(f"The first attempt in \"{word}\" is in index: {list.index(word, 2)}")
print(f"There are {list.count(word)} in \"{word}\"")

if word in list:
    print(f"\"{word}\" exists in the list within index: {list.index(word)}")
else: 
    print(f"Couldnt ifnd \"{word}\" in the list")
    

print("--------------------------------------------------")

liste = [3,22,5,46,8,9,12,6,1]
sorted_liste = sorted(liste)

print(f"Original list: {liste}")
print(f"Sorted list: {sorted_liste}")

liste.sort()
print(f"Original list after .sort(): {liste}")
    
sorted_liste.reverse()
print(f"Sorted list after .reverse(): {sorted_liste}")



print("--------------------------------------------------")

list1 = [1,2,3,4,5]
list2 = list1 # This becomes list1, where if list1 change, changes list2 too

print(f"{list1} and {list2}")

list2[0]=10 

print(f"{list1} and {list2}")

print(f"list1 is list2: {list1 is list2}")
print(f"list1 == list2: {list1 == list2}")


list3 = list1.copy() # This copies list1, where it is its own variable without being affected if list1 changes.

print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list3: {list1 == list3}")


list3[0]=1

print(f"\n{list1}, {list2}, {list3} \n")


print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list3: {list1 == list3}")
