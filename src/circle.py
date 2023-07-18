from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        if type(radius) is not int:
            raise TypeError('Wrong type')

        if radius <= 0:
            raise TypeError('Number cannot be less than or equal to 0')

        self.radius = radius
        self.number_pi = 3.14
        self.name = 'Circle'
        self.area = self.number_pi * radius * radius
        self.perimeter = (self.number_pi * radius) * 2

    def get_area(self):
        return self.area
