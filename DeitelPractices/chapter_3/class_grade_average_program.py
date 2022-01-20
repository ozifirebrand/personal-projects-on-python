total_grade = 0

counter = 0

grade = int(input("Enter the student's grade. -1 to end: "))


while grade != -1:
    total_grade += grade
    grade = int(input("Enter the student's grade. -1 to end: "))
    counter += 1

if counter != 0:
    average = total_grade / counter
    print(f'The average score is {average:.2f}')
