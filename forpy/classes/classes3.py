class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rectangle = Rectangle(4,5)
print(rectangle.area())

shape = Shape()
print(shape.area())