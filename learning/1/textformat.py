# tall = 12
# pi = 3.14159264

# print()
# print(f"--{tall:>10}--")   # Skriver ut variabelen 'tall' høyrejustert i en bredde på 10 tegn
# print(f"--{tall:<10}--")   # Skriver ut variabelen 'tall' venstrejustert i en bredde på 10 tegn
# print(f"--{tall:^10}--")   # Skriver ut variabelen 'tall' midtstilt i en bredde på 10 tegn
# print()

# print(f"{' Hei ':*>20}")    # Skriver ut teksten ' Hei ' høyrejustert i 20 tegn, fylt med '*'
# print(f"{' Hei ':*<20}")    # Skriver ut teksten ' Hei ' venstrejustert i 20 tegn, fylt med '*'
# print(f"{' Hei ':*^20}")    # Skriver ut teksten ' Hei ' midtstilt i 20 tegn, fylt med '*'
# print()

# print(f"--{pi:^10.2f}--")  # Skriver ut flyttallet 'pi' midtstilt i 10 tegn med 2 desimaler
# print(f"--{pi:^10.4f}--")  # Skriver ut flyttallet 'pi' midtstilt i 10 tegn med 4 desimaler
# print(f"--{pi:^10}--")     # Skriver ut variabelen 'pi' som standard (ingen desimalspesifikasjon), midtstilt i 10 tegn


# * 2)

# tall = 123
# print(f"{tall:b}") # b står for binary
# print(f"{tall:x}") # X står for hexadesimal

# * 3)

print()
print(f"       |---tall----|               |---binary---|           |---Hexadecimal---|")
print()
for i in range(1, 33):
    print(f"---{i:^20}-----" f"---{i:^20b}-----" f"---{i:^20x}---")


