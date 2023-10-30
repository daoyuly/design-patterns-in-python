

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a(self):
        "An abstract method A"

class ClassA(IA):
    def method_a(self):
        print("ClassA method_a")


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b(self):
        "An abstract method B"

class ClassB(IB):
    def method_b(self):
        print("ClassB method_B")

class ClassBAdapter(IA):
    def __init__(self):
        self.class_b = ClassB()
    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()

# The Client
# Before the adapter I need to test the objects class to know which
# method to call.
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()


# After creating an adapter for ClassB I can reuse the same method
# signature as ClassA (preferred)
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    item.method_a()