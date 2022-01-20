counter = 1
while counter <= 10:
    print(counter)
    counter += 1

number = 100
while number >= 100:
    number += 1
    if number % 17 == 0:
        print(number, 'is the first number divisible by 17 and greater than 100.')
        break
