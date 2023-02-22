import os
from random import randint
from Mob import Mob
from Player import Player

class Field():

    @property
    def player(self) -> Player:
        return self.__player
    
    @property
    def mobs(self) -> Mob:
        return self.__mobs
    
    def __init__ (self, player, mobs, size = 10):
        a = []
        [a.append(['_'] * size) for _ in range(size)]
        self.field = a
        self.__player = player
        self.__mobs = mobs
        self.size = size

    def display_info(self):
        os.system("CLS")
        print("-" * 50)
        [print(i) for i in self.field]


    def ran(self):
        return randint(0, self.size-1)
    
    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        self.player._place = self.generate()
        self.field[self.player._place[0]][self.player._place[1]] = self.player._sign
        for i in self.mobs:
            i._place = self.generate()
            self.field[i._place[0]][i._place[1]] = i._sign
    
        