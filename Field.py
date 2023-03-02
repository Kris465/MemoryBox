import os
from random import randint

from Player import Player


class Field:

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def mobs(self) -> list:
        return self.__mobs

    def __init__(self, player, mobs, size=10):
        self.field = [['_'] * size for _ in range(size)]
        self.__player = player
        self.__mobs = mobs if isinstance(mobs, list) else [mobs]
        self.size = size

    def display_info(self):
        os.system("CLS")
        print("-" * 50)
        [print(i) for i in self.field]

    def ran(self):
        return randint(0, self.size - 1)

    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        self.player._place = self.generate()
        self.field[self.player.place[0]][self.player.place[1]] = self.player.sign
        for i in self.mobs:
            i._place = self.generate()
            self.field[i.place[0]][i.place[1]] = i.sign
