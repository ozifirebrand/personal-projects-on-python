# User inputs three numbers
# The sum, average, product, smallest and largest of the numbers is
# determined.

print("Enter the three numbers whose arithmetic,largest and smallest is to be determined")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

print('Sum of', number_1, ',', number_2, '&', number_3, 'is', (number_1 + number_2 + number_3))
print('Average', 'is', (number_1 + number_2 + number_3) / 3)
print('Product', 'is', (number_1 * number_2 * number_3) / 3)

# number_1_is_greater = number_1 > number_2 and number_1> number_3
number_2_is_greater = number_2 > number_1 and number_2 > number_3
number_3_is_greater = number_3 > number_1 and number_3 > number_2

largest_number = number_1
if number_2_is_greater:
    largest_number = number_2
elif number_3_is_greater:
    largest_number = number_3
print('Largest number is', largest_number)
