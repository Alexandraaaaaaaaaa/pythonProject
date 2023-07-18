from abc import ABC

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c: int):
        if type(side_a) is not int or type(side_b) is not int or type(side_c) is not int:
            raise TypeError('Wrong type')

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('TriangleNotCreated')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        # вычисление полупериметра треугольника
        self.semi_perimeter = (side_a + side_b + side_c) / 2
        self.name = 'Triangle'
        self.area = (self.semi_perimeter * (self.semi_perimeter - side_a) * (self.semi_perimeter - side_b) * (
                self.semi_perimeter - side_c)) ** 0.5
        self.perimeter = side_a + side_b + side_c

    def get_area(self):
        return self.area
