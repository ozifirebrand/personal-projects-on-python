# Find the total of the numbers
# Divide the numbers by the number of numbers inputted
# Display average

total = 0
scores = [67, 56, 98, 39, 80, 72, 48, 23, 59, 90, 87]
for score in scores:
    total += score
print("The class total is", total)
print("The total number of students is", len(scores))
average = total / len(scores)
print("The class average is", average)
