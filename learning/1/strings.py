print("Tekst på en linje. \nTekst på neste linje") # \n = mellomrom
print()
print("Tekst på en linje. \n\nTekst på neste linje") # \n\n = to mellomrom

print("-------------------")

tall = input("Skriv inn et heltall: ")

if tall.isnumeric(): # Du kan sjekke hvis en input value er en tall gjennom isnumeric()
    print("Så bra at du skrev inn er heltall")
else: 
    print("Det du skrev var ikke en heltall")