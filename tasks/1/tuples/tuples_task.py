Tuple = "Have", "A", "Good", "Day"

# 1 For-løkke
print()
for i in Tuple:
    print(i)
    
# 2 While-løkke
print()
index = 0
while len(Tuple) > index:
    element = Tuple[index]
    print(element)
    index += 1

    
# 3 Uten løkke
print()
print(*Tuple, sep="\n")