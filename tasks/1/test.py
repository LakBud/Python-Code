# print()
# kolonne = int(input("Skriv hvor mange kolonner: "))
# rad = int(input("Skriv hvor mange rader: "))

# print()
# for i in range(1, rad+1):
#     for j in range(1, kolonne+1):
#         print(f"{(i * j):^2}", end=" ")
#     print()


# def hovedfunksjon(liste):
    
#     def finn_størst_tall(liste):
#         størst = liste[0]
#         for i in range(len(liste)):
#             if liste[i] > størst:
#                 størst = liste[i]
#         return størst
    
#     def finn_gjennomsnitt(liste):
#         total = 0
#         for element in liste:
#             total += element
#         gjennomsnitt = total / len(liste)
#         return gjennomsnitt
    
#     print(f"Gjennomsnitt: {finn_gjennomsnitt(liste)} | Størst Tall: {finn_størst_tall(liste)}")

# # Test
# l = [1,2,3,4,5,6,7,8,9,10]
# hovedfunksjon(l)

# input_bruker = input("Skriv inn en heltall (avslutt med q):  ")
# liste = []
# count = 0
# total = 0

# while input_bruker:

#     if input_bruker.isnumeric():
#         liste.append(int(input_bruker))
#         count += 1
        
#     elif input_bruker == "q":
        
#         if len(liste) == 0:
#             print("Ingen tall ble lagt til")
#             break
        
#         størst = liste[0]
#         minst = liste[0]
        
#         for i in range(len(liste)):
#             print(liste[i])
#             total += liste[i]
            
#             if liste[i] > størst:
#                 størst = liste[i]
                
#             if liste[i] < minst:
#                 minst = liste[i]
        
#         print()
#         print(f"Listen: {liste}")
#         print(f"Summen av alle elementene til sammen: {total}")
#         print(f"Det største elementen til listen: {størst}")
#         print(f"Det minste elementen til listen: {minst}")
#         print(f"Det er totalt {count} elementer i lista")
#         break
#     else:
#         print(f"ERROR ! | Du må enten skrive med heltall eller avslutte med q: ")
        
#     input_bruker = input("Skriv en annen heltall (avslutt med q): ")
        
        
# def main(liste):
#     l1 = []
#     l2 = []
    
#     for element in liste:
#         if element % 2 == 0:
#             l2.append(element)
#         else:
#             l1.append(element)
    
#     for i in range(len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i] > l1[j]:
#                 temp = l1[i]
#                 l1[i] = l1[j]
#                 l1[j] = temp
                
#     for i in range(len(l2)):
#         for j in range(i+1, len(l2)):
#             if l2[i] > l2[j]:
#                 temp = l2[i]
#                 l2[i] = l2[j]
#                 l2[j] = temp
                
#     return l1 + l2

# l = [1,2,3,4,5]

# print(main(l))


