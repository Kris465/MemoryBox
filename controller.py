import os
from random import randint



class Controller:
    def __init__(self, vc, player, mobs, field):
        self.view = vc
        self.player = player
        self.mobs = mobs
        self.field = field
        self.__display_info()

    def move(self, move):
        self.player.move(self.field, move)
        self.__display_info()

    def __display_info(self):
        self.view.display_info(self.field)

    def ran(self):
        return randint(0, self.field.size - 1)

    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        self.player.place = self.generate()
        self.field.field[self.player.place[0]][self.player.place[1]] = self.player.sign
        for i in self.mobs:
            i.place = self.generate()
            self.field.field[i.place[0]][i.place[1]] = i.sign
        self.__display_info()
