# 1. Input each test result (i.e., a 1 or a 2). Display the message “Enter result”
# each time the program requests another test result.
# 2. Count the number of test results of each type.
# 3. Display a summary of the test results indicating the number of students who
# passed and the number of students who failed.
# 4. If more than eight students passed the exam, display “Bonus to instructor.”

no_of_passes = 0
no_of_failures = 0
for student in range(10):
    exam_result = int(input("Enter the student's result: "))

    if exam_result == 1:
        no_of_passes += 1
    else:
        no_of_failures += 1

print(no_of_passes, "students passed!")
print(no_of_failures, "students failed!")

if no_of_passes >= 8:
    print("Well done! Bonus to teacher!")