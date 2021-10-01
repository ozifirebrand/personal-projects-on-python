class Circle:
    is_shape = True

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def __str__(self):
        return self.radius + " " + self.colour


# def create_circle():
first_circle = Circle("2", "blue")
second_circle = Circle("4", "red")

colour = first_circle.colour
colour2 = second_circle.colour
shape1 = first_circle.is_shape
second_circle.is_shape = False

print(colour)
print(colour2)
print(shape1)

print(first_circle)
print(second_circle)

print(first_circle.is_shape)


class Country:
    def __init__(self, name='Unspecified', population=None,
                 size=None):
        self.name = name
        self.population = population
        self.size = size


usa = Country(name='Ozi', population=567843332, size=3462756)

var = usa.__dict__

print(var)