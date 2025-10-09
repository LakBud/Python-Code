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

print("Dette programmet lar deg lage en liste med heltall.")
print("Når du er ferdig trykker du enter uten å skrive noe")

antall_tall = 0
tall_liste = []

while True:
  tekst_inn = input("Skriv inn et heltall: ")
  
  if tekst_inn == "":
    break
      
  if tekst_inn.isnumeric():
    tall = int(tekst_inn)
    tall_liste.append(tall)
    antall_tall +=1
    print(f"Du skrev inn tallet {tall}\n")
    
  else:
    print(f"{tekst_inn} er ikke et tall\n")
    
print(f"\nDu skrev inn {antall_tall} tall")
print(f"Du har nå laget en liste: {tall_liste}")