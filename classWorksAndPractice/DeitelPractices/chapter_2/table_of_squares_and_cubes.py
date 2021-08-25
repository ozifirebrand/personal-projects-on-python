print('number \t square \t cube')
print('0  \t\t', 0 ** 2, '\t\t\t', 0 ** 3)
print('1  \t\t', 1 ** 2, '\t\t\t', 1 ** 3)
print('2  \t\t', 2 ** 2, '\t\t\t', 2 ** 3)
print('3  \t\t', 3 ** 2, '\t\t\t', 3 ** 3)
print('4  \t\t', 4 ** 2, '\t\t', 4 ** 3)
print('5  \t\t', 5 ** 2, '\t\t', 5 ** 3)

# Using for loops
# Each of the values are incremented by 1
# The square and cubes of the values are computed
print()
print()

number = 0
print('number \t square \t cube')
while number <= 5:
    if number < 4:
        print(number, '\t\t', number ** 2, '\t\t\t', number ** 3)
    elif number >= 4:
        print(number, '\t\t', number ** 2, '\t\t', number ** 3)
    number += 1

# number = 4
# while number <= 5:
#     print(number, '\t\t', number ** 2, '\t\t', number ** 3)
#     number += 1
