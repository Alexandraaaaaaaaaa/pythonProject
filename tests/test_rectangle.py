import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('length, width, area, perimeter',
                         [
                             (78, 43, 3354, 242),
                             (2, 9, 18, 22)

                         ])
def test_rectangle(length, width, area, perimeter):
    r = Rectangle(length, width)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('length, width',
                         [
                             (0, 0),
                             (0, 1),
                             (1, 0),
                             (4, 0),
                             (-2, 9),
                             (3, -2),
                             (3, -2)
                         ])
def test_rectangle_negative_zero(length, width):
    with pytest.raises(ValueError):
        Rectangle(length, width)


@pytest.mark.parametrize('length, width',
                         [
                             ('flowers', 'cat'),
                             ({1, 4, 4}, {6, 2, 4}),
                             ([8, 1, 5], [8, 5, 5]),
                             (True, False),
                             (None, None)

                         ])
def test_rectangle_negative_type(length, width):
    with pytest.raises(TypeError):
        Rectangle(length, width)


@pytest.mark.parametrize('length, width, other_figure',
                         [
                             (4, 3, True),
                             (6, 5, None),
                             (2, 4, 'srt'),
                             (3, 4, 4)
                         ])
def test_rectangle_negative_add_area(length, width, other_figure):
    with pytest.raises(ValueError):
        rectangle = Rectangle(length, width)
        rectangle.add_area(other_figure)
