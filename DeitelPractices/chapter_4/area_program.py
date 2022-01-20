def rectangle_area(length_self, width):
    return length_self * width


def cuboid_volume(length_self, breadth_self, height_self):
    return length_self * breadth_self * height_self


length_of_rectangle = int(input('What is the length of the rectangle? '))
breadth_of_rectangle = int(input('What is the breadth of the rectangle? '))
print(rectangle_area(length_of_rectangle, breadth_of_rectangle))


length = int(input('What is the length of the cuboid? '))
breadth = int(input('What is the breadth of the cuboid? '))
height = int(input('What is the height of the cuboid? '))
print(cuboid_volume(length, breadth, height))
