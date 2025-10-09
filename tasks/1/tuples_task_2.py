
fruit = "apple", "bananna", "orange"
price = 10, 8, 12
enhet = "kg", "g", "mg"

combined = zip(fruit, price, enhet)

print(combined)
print(*combined)
print("--------------------")
for fruit, price, enhet in zip(fruit, price, enhet):
    print(f"The {fruit} costs {price} US dollars and weighs {enhet}")




