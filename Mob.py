from Character import Character
from random import randint


class Mob(Character):
    
    def __init__(self, clothes, hat):
        self.clothes = clothes
        self.hat = hat

        super().__init__(self)


    def shout():
        print("Arrrrrgh!")


    def prize():
        items = ["money", "health", "map", "key", "glue", "weapon", "speed"]
        item = items[randint(0, 6)]
        print(item)


    def buff():
        pass
