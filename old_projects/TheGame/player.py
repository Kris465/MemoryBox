from termcolor import colored
import character


class Player(character.Character):

    def __init__(self, name):
        self._hp = 100
        self._name = name
        self._attack = 10
        self._sign = "X"
        self._colour = 'blue'
        self._step = 1
        super().__init__(name, self._hp, self._attack, self._sign, self._colour, self._step)
