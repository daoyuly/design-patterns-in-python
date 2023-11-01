from abc import ABCMeta, abstractmethod
from  datetime import datetime
import  time


class ISwitch(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute(self):
        ""

class Light:

    @staticmethod
    def turn_on():
        print("Light turned ON")

    @staticmethod
    def turn_off():
        print("Light turned OFF")



class SwitchOffCommand(ISwitch):

    def __init__(self, light):
        self._light = light


    def execute(self):
        self._light.turn_off()


class SwitchOnCommand(ISwitch):

    def __init__(self, light):
        self._light = light


    def execute(self):
        self._light.turn_on()


class Switch:
    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        for cmd in self._history:
            print(
                f"{datetime.fromtimestamp(cmd[0]).strftime('%H:%M:%S')}"
                f": {cmd[1]}"
            )


    def register(self, cmd_name, command):
        self._commands[cmd_name] = command


    def execute(self, cmd_name):
        if cmd_name in self._commands.keys():
            self._commands[cmd_name].execute()
            self._history.append((time.time(), cmd_name))


    def replay_last(self, number_of_commands):
        commands = self._history[-number_of_commands]
        for cmd in commands:
            self._commands[cmd].execute()



light = Light()

switch_on = SwitchOnCommand(light)
switch_off = SwitchOffCommand(light)

switch = Switch()
switch.register('on', switch_on)
switch.register('off', switch_off)

switch.execute('on')
switch.execute('off')

switch.show_history()

switch.replay_last(2)

