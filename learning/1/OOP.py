# 1) Type
# tall = 12
# tekst = "Hei"
# liste = [1,2,3]

# def funksjon(x):
#     return x

# print(f"variabelen tall er av type {type(tall)}")
# print(f"variabelen tekst er av type {type(tekst)}")
# print(f"variabelen liste er av type {type(liste)}")
# print(f"funksjonen er av type {type(funksjon)}")

# 2) Classes

# class Person: # ? Oppretter en klasse
#     fornavn = "N"
#     etternavn = "N"
    
    
# person = Person() # ? Oppretter et object av klassen person
# person.etternavn = "Khan"

# print(f"Variabelen person er av type {type(person)}")
# print(f"Fornavn: {person.fornavn}. Etternavn: {person.etternavn}")

# 3) Bokstav endring
tekst = input("Skriv inn litt tekst så skal jeg gjøre noe med den: ")

print(f"Bare store bokstaver: {tekst.upper()}")
print(f"Bare lite bokstaver: {tekst.lower()}")
print(f"Alle ord får stor bokstav i starten: {tekst.title()}")
print(f"Det er {tekst.count("e")} forekomster av bokstaven e i teksten")
