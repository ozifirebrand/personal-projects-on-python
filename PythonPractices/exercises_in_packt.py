first_number = 24
second_number = 36
divisor = 24
while divisor >= 24:
    divisor += 1
    if divisor % first_number == 0 and divisor % second_number == 0:
        print(divisor, 'is the first lowest common multiple of 24 and 36')
        break