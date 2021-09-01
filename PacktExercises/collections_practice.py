
m = [[1, 2, 3], [4, 5, 6]]
for row in range(len(m)):
    for column in range(len(m[row])):
        print(m[row][column], end=' ')
    print()