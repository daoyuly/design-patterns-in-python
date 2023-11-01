from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute(self):
        "The required execute method that all command object will use"


class Invoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command
        return  self


    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"{command_name} not registered")



class Receiver:

    @staticmethod
    def run_command_1(self):
        print("Execute command 1")

    @staticmethod
    def run_command_2(self):
        print("Execute command 2")


class Command1(ICommand):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()


class Command2(ICommand):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()



#client
receiver = Receiver()

command1 = Command1(receiver)
command2 = Command2(receiver)


invoker = Invoker()
invoker.register("1", command1).register("2", command2)

invoker.execute("1")
invoker.execute("2")