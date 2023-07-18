import pytest
from src.square import Square
from src.figure import Figure


@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (4, 16, 16)
                         ])
def test_square(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == 'Square'
    assert s.area == area
    assert s.perimeter == perimeter


@pytest.mark.parametrize('side_a',
                         [
                             'fee',
                             {1, 2},
                             [8, 1],
                             True,
                             None

                         ])
def test_square_negative_type(side_a):
    try:
        Square(side_a)
    except TypeError:
        assert True


@pytest.mark.parametrize('side_a',
                         {
                             0, -1

                         })
def test_square_negative_side(side_a):
    try:
        Square(side_a)
    except ValueError:
        assert True


@pytest.mark.parametrize('side_a, other_figure',
                         [
                             (4, True),
                             (6, None),
                             (2, 'srt'),
                             (3, 4)
                         ])
def test_square_negative_add_area(side_a, other_figure):
    try:
        circle = Square(side_a)
        circle.add_area(other_figure)
    except ValueError:
        assert True
