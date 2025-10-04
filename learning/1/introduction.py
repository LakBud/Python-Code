
# Oppgave 1:

# Programmet ber om et heltall (int) som bestemmer "max"

max = int(input("Enter a whole Number: "))
sum = 0


# Fra 1 til "max" (bestemmes av i), skal "sum" plusse med "sum" og antall ganger den kjører (i).


for i in range(1, max + 1):
    sum = sum + i


# Hvis "sum" er større enn 1000, printes det "sum".

if (sum > 1000):
    print(f"The sum of the whole numbers is: {sum}")

# Hvis "sum" oppfyller ikke kravene til if-setningen, skal det ikke printe "sum"

else:
    print("Sum is not higher then 1000")





