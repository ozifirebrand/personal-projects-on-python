
data = []
fruits = ["apple", "banana", "orange"]
number_of_fruit_at_first =[5, 8, 9]
number_of_fruit_at_second = [7, 6, 2]

data.append(fruits)
data.append(number_of_fruit_at_first)
data.append(number_of_fruit_at_second)

for row in data:
    for index_2 in row:
        print(index_2, end=" ")
    print()

print()

numbers = [[1, 2, 3], [4, 5, 6]]
for number in numbers:
    for column in number:
        print(column, end=" ")
    print()

user_data_1 = ["John Mckee", 38, "Sales"]
user_data_2 = ["Lisa Crawford", 29, "Marketing"]
user_data_3 = ["Sujan Patel", 33, "HR"]

user_data = [user_data_1, user_data_2, user_data_3]
print()
for user in user_data:
    for info in user:
        print(info, end=" ")
    print()

print()
for user in user_data:
    print(user)
    print("Name:", user[0])
    print("Age:", user[1])
    print("Department", user[2])
    print("_" * 20)

x_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y_matrix = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
result = [[0, 0, 0, ], [0, 0, 0], [0, 0, 0]]
for row in range(len(x_matrix)):
    for column in range(len(x_matrix[0])):
        result[row][column] = x_matrix[row][column] + y_matrix[row][column]


print(result)


native_1 = [[4, 22, 10], [5, 20, 11]]
native_2 = [[6, 24, 15], [34, 51, 66]]

cohort_members = [native_1, native_2]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(len(native_1)):
    for column in range(len(native_1[0])):
        result[row][column] = native_1[row][column] + native_2[row][column]


print(result)
