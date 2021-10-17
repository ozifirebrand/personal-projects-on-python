country_codes = {'Finland': 'fi',
                'South Africa': 'za',
                'Nepal': 'np'}

for value in country_codes.keys():
    print(value)


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