from abc import ABCMeta,abstractmethod

class IAbstraction(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args):
        "the method handle"


class IImplementer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args: tuple):
         "The method implementation"


class ConcreateImplementerA(IImplementer):
    def method(self, *args: tuple) -> None:
        print(args)


class ConcreateImplementerB(IImplementer):
    def method(*args: tuple):
        for arg in args:
            print(arg)

class RefinedAbstractionA(IAbstraction):

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(args)


class RefinedAbstractionB(IAbstraction):
    def __init__(self, implementer):
        self.implementer = implementer

    def method(self, *args):
        self.implementer.method(args)


# client
refined_abstraction_a = RefinedAbstractionA(ConcreateImplementerA)
refined_abstraction_a.method(['a', 'b', 'c'])

refined_abstraction_b = RefinedAbstractionB(ConcreateImplementerB)
refined_abstraction_b.method(['1', '2', '3'])