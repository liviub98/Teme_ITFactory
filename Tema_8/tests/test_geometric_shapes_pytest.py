import pytest
from Teme_ITF.Tema_8.app.geometric_shapes import Square, Rectangle, Circle


class TestSquare:
    @pytest.mark.parametrize('value, expected', [
        (10.5, 110.25),
        (9, 81)
    ])
    def test_area(self, value, expected):
        square = Square(value)
        assert square.area() == expected

    @pytest.mark.parametrize("value, expected", [
        (5, 20),
        (2.5, 10)
    ])
    def test_perimeter(self, value, expected):
        square = Square(value)
        assert square.perimeter() == expected


class TestRectangle:
    @pytest.mark.parametrize("length, width, expected", [
        (10, 5, 50),
        (2.5, 3.2, 8)
    ])
    def test_area(self, length, width, expected):
        rectangle = Rectangle(length, width)
        assert rectangle.area() == expected

    @pytest.mark.parametrize("length, width, expected", [
        (10, 5, 30),
        (3.5, 6.2, 19.40)
    ])
    def test_perimeter(self, length, width, expected):
        rectangle = Rectangle(length, width)
        assert rectangle.perimeter() == expected


class TestCircle:
    @pytest.mark.parametrize("radius, expected", [
        (10, 314.159),
        (1, 3.142)
    ])
    def test_area(self, radius, expected):
        circle = Circle(radius)
        rounded = round(circle.area(), 3)
        assert rounded == expected

    @pytest.mark.parametrize("radius, expected", [
        (2, 12.566),
        (3, 18.85)
    ])
    def test_perimeter(self, radius, expected):
        circle = Circle(radius)
        rounded = round(circle.perimeter(), 3)
        assert rounded == expected
