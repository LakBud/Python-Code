
# * 1)

print("V")
print("e")
print("r")
print("t")
print("i")
print("k")
print("a")
print("l")

print("-------------")

print("V\ne\nr\nt\ni\nk\na\nl\n")



print("-------------")


# ? 2)

grunnlinje_str = input("Skriv et tall for grunnlinjen: ")
høyde_str = input("Skriv et tall for høyden: ")

if grunnlinje_str.isnumeric() and høyde_str.isnumeric():
    grunnlinje = int(grunnlinje_str)
    høyde = int(høyde_str)
    trekant = (grunnlinje * høyde)

    slutt_tall = int(input("Hvor mange ganger skal summen gjentas? "))
    sum = 0
    for i in range(slutt_tall):
        sum += trekant

    print(sum)
else:
    print("Du skrev ikke inn riktige tall")
