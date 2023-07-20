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
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a',
                         [
                             'fee',
                             {1, 2},
                             [8, 1],
                             True,
                             None

                         ])
def test_square_negative_type(side_a):
    with pytest.raises(TypeError):
        Square(side_a)


@pytest.mark.parametrize('side_a',
                         {
                             0, -1

                         })
def test_square_negative_side(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize('side_a, other_figure',
                         [
                             (4, True),
                             (6, None),
                             (2, 'srt'),
                             (3, 4)
                         ])
def test_square_negative_add_area(side_a, other_figure):
    with pytest.raises(ValueError):
        square = Square(side_a)
        square.add_area(other_figure)
