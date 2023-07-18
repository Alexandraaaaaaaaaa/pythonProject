from src.figure import Figure


class Square(Figure):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError('SquareNotCreated')

        if type(side_a) is not int:
            raise TypeError('Wrong type')

        self.name = 'Square'
        self.area = side_a ** 2
        self.perimeter = side_a * 4

    def get_area(self):
        return self.area
