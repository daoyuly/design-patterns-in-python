from abc import  ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    "the builder interface"

    @staticmethod
    @abstractmethod
    def build_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def build_result():
        "Build result"


class Builder(IBuilder):

    def __init__(self):
        self.product = Product()

    def build_a(self):
        self.product.addPart('a')
        return self

    def build_b(self):
        self.product.addPart('b')
        return self

    def build_c(self):
        self.product.addPart('c')
        return self

    def build_result(self):
        self.product.getParts()

class Product:

    def __init__(self):
        self.__parts = []

    def addPart(self, part):
        self.__parts.append(part)

    def getParts(self):
        return self.__parts



class Director:
    "the director, building a complex representation"

    @staticmethod
    def construct():
        return  (Builder
                 .build_a()
                 .build_b()
                 .build_c()
                 .build_result())



# client
product = Director.construct()
print(product)