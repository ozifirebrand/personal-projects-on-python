# Assume that the tax on a restaurant bill is 6.25% and that the
# bill amount is $37.45. Use type Decimal to calculate the bill
# total, then print the result with two digits to the right of the
# decimal point.
from decimal import Decimal
from statistics import *

print(f"{Decimal('37.45') * Decimal('1.0625'):.2f}")

# COMPARISON OF VALUES
i, j, k, m = 1, 2, 3, -2
var = i >= 1 and j < 4
print(var)
var = 99 >= m > k
print(var)
var = j >= i or k == m
print(var)
var = (k + m < j) or (3 - j >= k)
print(var)
var = not (k > m)
print(var)

# SUM AND AVERAGE OF GRADES
grades_of_students = [85, 93, 45, 89, 85]
print(sum(grades_of_students)/len(grades_of_students))
print(mean(grades_of_students))
print(mode(grades_of_students))
print(median(grades_of_students))