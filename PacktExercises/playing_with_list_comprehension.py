numbers = [2, 4, 5, 6, 8, 9, 90]
lucky_numbers = []
for number in numbers:
    if number % 2 == 0:
        lucky_numbers.append(number)

print(lucky_numbers)

lucky_numbers = [number for number in numbers if number % 2 == 0]
print(lucky_numbers)

# Saw this somewhere and thought to replicate