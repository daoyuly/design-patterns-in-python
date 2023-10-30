class Singleton(type):

    def __init__(self):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance == None:
            self.__instance = super().__call__(*args, **kwargs)
            return  self.__instance
        else:
            return self.__instance

class MyClass(metaclass==Singleton):
    pass

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a == b)
    print(a is b)
    print(a, b)