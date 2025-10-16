# print()
# kolonne = int(input("Skriv hvor mange kolonner: "))
# rad = int(input("Skriv hvor mange rader: "))

# print()
# for i in range(1, rad+1):
#     for j in range(1, kolonne+1):
#         print(f"{(i * j):^2}", end=" ")
#     print()


def hovedfunksjon(liste):
    
    def finn_størst_tall(liste):
        størst = liste[0]
        for i in range(len(liste)):
            if liste[i] > størst:
                størst = liste[i]
        return størst
    
    def finn_gjennomsnitt(liste):
        total = 0
        for element in liste:
            total += element
        gjennomsnitt = total / len(liste)
        return gjennomsnitt
    
    print(f"Gjennomsnitt: {finn_gjennomsnitt(liste)} | Størst Tall: {finn_størst_tall(liste)}")

# Test
l = [1,2,3,4,5,6,7,8,9,10]
hovedfunksjon(l)
