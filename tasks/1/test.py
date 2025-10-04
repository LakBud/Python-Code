# 1

# tall1 = float(input("Skriv et tall: "))
# tall2 = float(input("Skriv et annet tall: "))

# if ((tall1 + tall2) > 10):
#     print("Over 10")
# else:
#     print("Under 10")



# 2
# list = [1,2,3,4,5,6,7,8,9,10]

# heltall = int(input("Skriv inn et heltall: "))


# for element in list:
#     print(int(element) * heltall)
    

# 3
# print()
# for row in range(1,11):
#     for column in range(1,11):
#         print(f"{row * column:4}", end="")
#     print()
    

# 6
t = "Hei på deg"
l = list(t)

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            t = l[j]
            l[j] = l[i]
            l[i] = t
print(l)