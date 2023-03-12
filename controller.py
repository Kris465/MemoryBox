from random import randint

from character import Character
from field import Field
from mob import Mob
from player import Player


class Controller:

    def __init__(self):
        self.field = None
        self.init_units()

    def get_field(self):
        return self.field

    def set_field(self, field):
        self.field = field

    @staticmethod
    def get_characters():
        return Character.characters

    def review(self):
        for ch in self.get_characters():
            ch.review_attr = ch.review()

    def attack(self):
        self.review()
        for ch in self.get_characters():
            if isinstance(ch, Player):
                return ch.attack()

    def is_dead(self):
        self.field_update()
        [self.get_characters().remove(ch) for ch in self.get_characters() if ch.hp <= 0]

    def move(self, move_side):
        self.review()
        for ch in self.get_characters():
            if isinstance(ch, Player):
                ch.move(self.field, move_side, ch.review_attr)
        self.field_update()

    def field_update(self):
        for character in self.get_characters():
            place = character.place
            self.field.field[place[0]][place[1]] = character.sign

    def ran(self):
        print(self.field)
        return randint(0, self.field.size - 1)

    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        Player('lameR')
        [Mob("Шляпа", "Платье") for _ in range(5)]
        self.field = Field()
        for ch in self.get_characters():
            ch.place = self.generate()
            self.field.field[ch.place[0]][ch.place[1]] = ch.sign
