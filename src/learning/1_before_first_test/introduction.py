
# Task 1:

# Programmet ber om et heltall (int) som bestemmer "max"

max = int(input("Enter a whole Number: "))
sum = 0


# From 1 to "max" (stored in i),  "sum" should plus with its self and i.


for i in range(1, max + 1):
    sum = sum + i


# If "sum" is bigger then 1000, it prints out "sum".

if (sum > 1000):
    print(f"The sum of the whole numbers is: {sum}")

# If "sum" doesnt go through, it should print something else

else:
    print("Sum is not higher then 1000")





