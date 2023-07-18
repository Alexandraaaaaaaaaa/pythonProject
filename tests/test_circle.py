import pytest
from src.circle import Circle
from src.figure import Figure


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (2, 12.56, 12.56),
                             (5, 78.5, 31.400000000000002)

                         ])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == 'Circle'
    assert c.area == area
    assert c.perimeter == perimeter


@pytest.mark.parametrize('radius',
                         [
                             'fee',
                             {1, 2},
                             [8, 1],
                             True,
                             None

                         ])
def test_circle_negative_type(radius):
    try:
        Circle(radius)
    except TypeError:
        assert True


@pytest.mark.parametrize('radius',
                         {
                             0, -1

                         })
def test_circle_negative_radius(radius):
    try:
        Circle(radius)
    except TypeError:
        assert True


@pytest.mark.parametrize('radius, other_figure',
                         [
                             (4, True),
                             (6, None),
                             (2, 'srt'),
                             (3, 4)
                         ])
def test_circle_negative_add_area(radius, other_figure):
    try:
        circle = Circle(radius)
        circle.add_area(other_figure)
    except ValueError:
        assert True
