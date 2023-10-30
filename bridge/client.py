from abc import ABCMeta, abstractmethod

class IShape(metaclass=ABCMeta):
    @abstractmethod
    @staticmethod
    def draw():
        "The method that will be handled at the shapes implementer "

class IShapeImplementer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def draw_implementer():
        "the method that the refined abstraction will implement"


class CircleImplementer(IShapeImplementer):
    def draw_implementer(self):
        print("    ******")
        print("  **      **")
        print(" *          *")
        print("*            *")
        print("*            *")
        print(" *          *")
        print("  **      **")
        print("    ******")


class SquareImplementer(IShapeImplementer):
    def draw_implementer(self):
        print("**************")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("*            *")
        print("**************")

class Circle(IShape):

    def __init__(self, implementer):
        self.implementer = implementer

    def draw(self):
        self.implementer.draw_implementer()


class Square(IShape):
    def __init__(self, implementer):
        self.implementer = implementer

    def draw(self):
        self.implementer.draw_implementer()



circle = Circle(CircleImplementer)
circle.draw()

square = Square(SquareImplementer)
square.draw()