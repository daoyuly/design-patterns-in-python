import random
from abc import ABCMeta, abstractmethod

class IHandler(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def handle(payload):
        "method to implement"


class Successor1(IHandler):

    @staticmethod
    def handle(payload):
        print(f"Successor={payload}")
        test = random.randint(1, 2)
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload


class Successor2(IHandler):

    @staticmethod
    def handle(payload):
        print(f"Successor={payload}")
        test = random.randint(1, 2)
        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload)
        return payload



class Chain():

    @staticmethod
    def start(payload):
        return Successor1().handle(payload)
