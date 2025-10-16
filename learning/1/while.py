tall = int(input("Skriv inn et heltall: "))

count = 1
summen = 0


while count < tall+1:
    summen += count
    count += 1

print(f"Summen av positive heltall fra 1 til {tall} er {summen}")
