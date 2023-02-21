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
    
    def __init__ (self, player, mob):
        self.field = [["*" * 5] for i in range(5)]
        self.field.insert(0, self.__player.name)
        self.field.insert(randint(0, 25), self.__mob.name)

    def display_info(self):
        [print(i) for i in self.field] 

