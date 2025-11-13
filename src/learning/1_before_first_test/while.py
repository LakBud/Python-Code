number = int(input("Write a whole number: "))

count = 1
total_sum = 0


while count < number+1:
    total_sum += count
    count += 1

print(f"total_sum of positive integer from 1 to {number} is {total_sum}")
