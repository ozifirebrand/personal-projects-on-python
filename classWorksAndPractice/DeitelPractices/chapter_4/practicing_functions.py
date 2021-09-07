def square(number):
    """Calculate the square of number."""
    return number ** 2


def square_root(number):
    """Calculate the square root of a number"""
    return number ** 0.5


def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


def minimum(value1, value2, value3):
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value


print(square(7))
print(square(2.5))
print(square_root(16))
print(maximum(7, 2, 8))
print(maximum(74, 72, 8))
print(maximum(7, 2, 60))
print(maximum(-7, -2, -18))
print(maximum("Yellow", "Grey", "Happy"))
print(minimum(5, 6, 4))
