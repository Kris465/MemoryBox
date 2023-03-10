from Character import Character
from random import randint


class Mob(Character):
    
    def __init__(self, clothes, hat):
        self._name = 'Mob'
        self._base_hp = 100
        self._hp = self._base_hp
        self._attack = 10
        self._sign = "#"
        self.clothes = clothes
        self.hat = hat

        super().__init__(self)


    def shout(self):
        print("Arrrrrgh!")


    def prize(self):
        items = ["money", "health", "map", "key", "glue", "weapon", "speed"]
        item = items[randint(0, 6)]
        print(item)


    def buff(self):
        pass
