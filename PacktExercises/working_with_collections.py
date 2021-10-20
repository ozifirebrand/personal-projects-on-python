# todo - A dictionary

country_codes = {'Finland': 'fi',
                'South Africa': 'za',
                'Nepal': 'np'}

for value in country_codes.keys():
    print(value)

# fixme - A list

shopping = ['Apple', 'Eggs', 'Yam', 'Boli', 'Tuwo']

print(shopping)

shopping.insert(3, 'Coconut')
shopping.pop(2)
print(shopping)

employee = {
    "name" : "Bolanle Shola",
    "age" : 33,
    "department" : "Electrical and Electronics Engineering"
}

print(employee)

movie = {
    'title' : 'The Godfather',
    'director' : 'Francis Ford Coppola',
    'year' : 1972,
    'rating' : 9.2
}

print(movie['year'])
print(movie['title'])
print(movie['director'])
print(movie['rating'])
print(movie)

movie_2 = {}
movie_2['title'] = 'Abejoye'
movie_2['year'] = 2021
movie_2['director'] = 'Mike Bamiloye'
movie_2['rating'] = 9.0

print(movie_2)

employees = [{'name' : 'Mojoyin Oketope',
              'age' : 10,
              'department' : 'Project Manager'},
            {'name' : 'Jerry Ifeanyi',
              'age' : 12,
              'department' : 'Backend Developer'},
             {'name' : 'Gideon Udoh',
              'age' : 16,
              'department' : 'Frontend Developer'}
             ]

print(employees)
for employee_ in employees:
    print("Name :", employee_['name'])
    print("Age :", employee_['age'])
    print("Department :", employee_['department'])


items = ['omo','bottle water', 'ginger', 'dangote sugar']
quantity = [1, 12, 15, 2]

# fixme - Mapping items in a list using zip

orders = zip(items, quantity)
print(list(orders))

orders = zip(items, quantity)
print(dict(orders))
print()

orders = zip(items, quantity)
print(tuple(orders))
print()

orders = {'crayfish' : 5, 'ede': 3, 'azu ikpo' : 6}
print(orders.values())
print()

print(list(orders.values()))
print()

print(list(orders.keys()))
print()


for tuple_ in list(orders.items()):
    print(tuple_)

t_mixed = 'jangi-lova', 'baflit', 'bendankari'
print(t_mixed)
print()
print(t_mixed + ('ten-ten','suwe') )
print()

t_shopping_list = ('wig', 'hair clip', 'hair band'), ('lace glue', 'ilarun', 'expression attachment')
print(t_shopping_list)

set_1 = {1, 2, 3, 4}
set_2 ={1, 2, 4, 3, 4, 5, 6, 5, 2}
set_3 = {8, 6,3,1 ,5,2,5,6,8}
print()
print(set_1)
print(set_2)
print(set_3)

set_4 = {'boli', 'suya', 'epa'}
print()
print(set_4)
print()
set_4.add('fura')
print(set_4)

print()
print(set_1 | set_2)
print(set_1.union(set_2))
print()
print(set_1 & set_2)
print(set_1.intersection(set_2))
print()
print(set_1 <= set_3)
print(set_1.issubset(set_3))
print()
print(set_1 <= set_2)
print(set_1.issubset(set_2))