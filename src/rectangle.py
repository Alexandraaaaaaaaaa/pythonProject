from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width: int):

        if type(length) is not int or type(width) is not int:
            raise TypeError('Wrong type')

        if length <= 0 or width <= 0:
            raise ValueError('RectangleNotCreated')

        self.length = length
        self.width = width
        self.name = 'Rectangle'
        self.area = length * width
        self.perimeter = (length + width) * 2

    def get_area(self):
        return self.area
