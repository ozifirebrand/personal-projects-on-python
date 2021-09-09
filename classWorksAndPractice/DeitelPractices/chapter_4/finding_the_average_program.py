def average(*args):
    # args += int(input())
    return sum(args) / len(args)


print(average(5, 3, 6, 8, 9))
print(average(5, 6, 8, 9))


def calculate_product(*argument_list):
    new_product = 1
    for product in argument_list:
        new_product *= product
    return new_product


print(calculate_product(10, 20, 30))

