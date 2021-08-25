# We want to determine if the number is a multiple of another number
# To do this, we check if that if we divide the smaller number with the bigger number, it is zero
# If it gives us zero, we say that number is a multiple of the big number
# If it doesn't give zero, then it is not a multiple of the big number


number = int(input('Type a number to determine if 2 is its multiple: '))
if number % 2 == 0:
    print('2 is a multiple of', number)
else:
    print('2 is not a multiple of', number)
