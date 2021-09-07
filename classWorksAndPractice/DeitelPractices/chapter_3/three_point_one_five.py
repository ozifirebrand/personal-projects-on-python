# e = 1+ 1/1!+ 1/2!+1/3!+...
# the program sums the individual values gotten from dividing
#   one by the factorials
#   and those lesser than them

# The factorials are calculated
# The factorials are gotten by multiplying the numbers by
#   numbers lesser to them by one until we get to the number ten

# The factorials divide 1
# The numbers are summed
factorial = 1
first_sum = 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    new_factorial = factorial * number

    first_division = (1 / factorial)

    new_first_sum = first_sum + first_division

    print('Current factorial : %5.2f' % new_factorial )
    print('Current sum : %3.4f' % new_first_sum)
    first_sum = new_first_sum
    factorial = new_factorial
