

data = []
fruits = ["apple", "banana", "orange"]
number_of_fruit_at_first =[5, 8, 9]
number_of_fruit_at_second = [7, 6, 2]

data.append(fruits)
data.append(number_of_fruit_at_first)
data.append(number_of_fruit_at_second)

for index in data:
    for index_2 in index:
        print(index_2, end=" ")
    print()