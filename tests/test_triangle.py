import pytest
from src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter',
                         [
                             (3, 4, 5, 6, 12)
                         ])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == 'Triangle'
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0, 0, 0),
                             (0, 1, 4),
                             (1, 0, 6),
                             (2, 4, 0),
                             (-2, 9, 3),
                             (3, -2, 4),
                             (3, 3, -2)
                         ])
def test_triangle_negative_zero(side_a, side_b, side_c):
    try:
        Triangle(side_a, side_b, side_c)
    except ValueError:
        assert True


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             ('fee', 'mew', 'poo'),
                             ({1, 4, 4}, {6, 2, 4}, {2, 2, 9}),
                             ([8, 1, 5], [8, 5, 5], [8, 2, 5]),
                             (True, False, True),
                             (None, None, None)

                         ])
def test_triangle_negative_type(side_a, side_b, side_c):
    try:
        Triangle(side_a, side_b, side_c)
    except TypeError:
        assert True


@pytest.mark.parametrize('side_a, side_b, side_c, other_figure',
                         [
                             (4, 3, 5, True),
                             (6, 5, 6, None),
                             (2, 4, 2, 'srt'),
                             (3, 4, 1, 4)
                         ])
def test_triangle_negative_add_area(side_a, side_b, side_c, other_figure):
    try:
        triangle = Triangle(side_a, side_b, side_c)
        triangle.add_area(other_figure)
    except ValueError:
        assert True
