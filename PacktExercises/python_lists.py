# shopping_items = ['Food', 'Clothe', 'Electronics', 'Car']
#
# for item in shopping_items:
#     if item in shopping_items[3]:
#         print(item)
#     if item not in shopping_items[3]:
#         print(item, end=', ')

mixed = [365, 'days', True]

for mix in mixed:
    if mix != mixed[2]:
        print(mix, end=', ')
    if mix == mixed[2]:
        print(mix, end='')
