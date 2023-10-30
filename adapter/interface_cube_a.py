from abc import ABCMeta, abstractmethod

class ICubeA(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def manufacture(width, height, depth):
         "manufactures a cube"
