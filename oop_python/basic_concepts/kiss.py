from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate(self):
        return self.shape.area()


rectangle = Rectangle(5, 10)
calculator = AreaCalculator(rectangle)
print(calculator.calculate())
