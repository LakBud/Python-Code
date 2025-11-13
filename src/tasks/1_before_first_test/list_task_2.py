rows = int(input("How many rows do you want: "))
columns = int(input("How many columns do you want: "))
print()

xo_list = []

for row in range(rows):
    for col in range(columns):
        if (row + col) % 2 == 0:
            xo_list.append("X")
        else:
            xo_list.append("O")


for i in range(rows):
    for j in range(columns):
        print(f"{xo_list[i * columns + j]:^2}", end="")
    print()
