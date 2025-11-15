# number = 12
# pi = 3.14159264

# print()
# print(f"--{number:>10}--")   # Writes out the variable 'number' right-adjusted with en bredde på 10 tegn
# print(f"--{number:<10}--")   # Writes out the variable 'number' left-adjusted with en bredde på 10 tegn
# print(f"--{number:^10}--")   # Writes out the variable 'number' midtstilt with en bredde på 10 tegn
# print()

# print(f"{' Hei ':*>20}")    # Writes out the text ' Hei ' right-adjusted with 20 tegn, fylt med '*'
# print(f"{' Hei ':*<20}")    # Writes out the text ' Hei ' left-adjusted with 20 tegn, fylt med '*'
# print(f"{' Hei ':*^20}")    # Writes out the text ' Hei ' midtstilt with 20 tegn, fylt med '*'
# print()

# print(f"--{pi:^10.2f}--")  # Writes out the float variable 'pi' in the middle with 10 symbols and 2 decimals
# print(f"--{pi:^10.4f}--")  # Writes out the float variable 'pi' in the middle with 10 symbols and 4 decimals
# print(f"--{pi:^10}--")     # Writes out the float variable 'pi' as standard (no desimal), in the middle with 10 symbols


# * 2)

# number = 123
# print(f"{number:b}") # b stands for binary
# print(f"{number:x}") # X stands for hexadesimal

# * 3)

print()
print(f"       |---number----|               |---binary---|           |---Hexadecimal---|")
print()
for i in range(1, 33):
    print(f"---{i:^20}-----" f"---{i:^20b}-----" f"---{i:^20x}---")


