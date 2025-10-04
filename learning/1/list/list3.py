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

# liste.index(element): finner og returner indeksten (plasseringen) til det først element som finnes i lista. Hvis det ikke finnes får man en feilmelding.
# liste.index(element: index): gjør det samme, men starter fra en gitt indeks (plassering)
# element in liste: sjekker om elementet finnes i lista (kan brukes i while/if-setninger)
# liste.count(element): returnerer antall forekomster av elemente lista.

list = ["A", "B", "C", "D", "C", "B", "A"]
word = "A"
print(f"Det første treff på \"{word}\" er på index: {list.index(word)}")
print(f"Det første treff på \"{word}\" er på index: {list.index(word, 2)}")
print(f"Det er {list.count(word)} forekomster av  \"{word}\" i lista")

if word in list:
    print(f"\"{word}\" finnes i lista på indesk: {list.index(word)}")
else: 
    print(f"Finner ikke \"{word}\" i lista")
    

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
list2 = list1 # Det blir selveste list1, hvor hvis list1 endres, endres også list2

print(f"{list1} og {list2}")

list2[0]=10 

print(f"{list1} og {list2}")

print(f"list1 is list2: {list1 is list2}")
print(f"list1 == list2: {list1 == list2}")


list3 = list1.copy() # Dette KOPIERER list1, hvor det er IKKE selveste list1 og kan ha endringer uten list1.

print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list3: {list1 == list3}")


list3[0]=1

print(f"\n{list1}, {list2}, {list3} \n")


print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list3: {list1 == list3}")
