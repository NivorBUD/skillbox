import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def init(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def area(self):
        p = (self.first_side + self.second_side + self.third_side) / 2.0
        return math.sqrt(p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side))


