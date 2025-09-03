import random
from typing import Any

from termcolor import colored

from field import Field
from move import Move


class Character:
    characters = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def full_hp(self) -> int:
        return self._base_hp

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def attack_power(self) -> int:
        return self._attack

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, item):
        self._place = item

    @property
    def sign(self):
        return self._sign
    
    @property
    def colour(self):
        return self._colour

    def __init__(self, name: str, hp: int, attack: int, sign: str, colour: str, step: int) -> None:
        self._name = name
        self._base_hp = hp
        self._hp = self._base_hp
        self._attack = attack
        self._sign = sign
        self._colour = colour
        self._step = step
        self._place = None
        self.review_attr: dict = {}
        self.characters.append(self)

    def attack(self) -> Any | None:
        damage = random.randint(0, self._attack)
        for character in self.characters:
            for key in self.review_attr.keys():
                if key != 'cp' and self.review_attr[key] == character.place:
                    return character.get_damage(damage)
        return None

    def get_damage(self, damage: int):
        self._hp -= damage
        if self._hp <= 0:
            self._sign = '-'
        return self

    def _move_side(self, field: Field, pos_cur, pos_new):
        if 0 <= pos_new[0] <= field.size - 1 and 0 <= pos_new[1] <= field.size - 1:
            field.field[pos_new[0]][pos_new[1]] = self._sign
            field.field[pos_cur[0]][pos_cur[1]] = '-'
            self._place = pos_new
        else:
            field.field[pos_cur[0]][pos_cur[1]] = self._sign
        return field

    def move(self, field, move, review: dict):
        match move:
            case Move.LEFT.value:
                return self._move_side(field, review['cp'], review['left'])
            case Move.DOWN.value:
                return self._move_side(field, review['cp'], review['down'])
            case Move.UP.value:
                return self._move_side(field, review['cp'], review['up'])
            case Move.RIGHT.value:
                return self._move_side(field, review['cp'], review['right'])

    def review(self):
        step = self._step
        cp = {}
        x, y = self._place
        cp['cp'] = self._place
        cp['left'] = [x, y - step]
        cp['down'] = [x + step, y]
        cp['up'] = [x - step, y]
        cp['right'] = [x, y + step]
        return cp
