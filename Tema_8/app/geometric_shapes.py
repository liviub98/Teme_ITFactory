from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi


class GeometricShape(ABC):
    PI = pi

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


@dataclass
class Square(GeometricShape):
    latura: float

    def area(self):
        return self.latura ** 2

    def perimeter(self):
        return self.latura * 4


@dataclass
class Rectangle(GeometricShape):
    length: float
    width: float

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


@dataclass
class Circle(GeometricShape):
    radius: float

    def area(self):
        return self.PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * (self.PI * self.radius)
