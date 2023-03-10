import random
from move import Move


class Character:

    @property
    def name(self) -> int:  # возможно тут надо стринг
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

    def __init__(self, character) -> None:
        self._name = '' if character._name is None else character._name
        self._base_hp = character._hp
        self._hp = self._base_hp
        self._attack = character._attack
        self._sign = character._sign
        self._place = None

    def attack(self, character):
        damage = random.randint(0, self._attack)
        character.__get_damage(damage)

    def __get_damage(self, damage):
        self._hp -= damage

    def move_type(self, field, move):
        if move == Move.UP:
            pass
        elif move == Move.DOWN:
            pass
        elif move == Move.LEFT:
            pass

    def move(self, field, move):

        position = self._place
        # print(field.field)
        field.field[self._place[0]][self._place[1]] = '_'
        field.field[position[0] - 1][position[1]] = self._sign

        print(field.field[position[0]][position[1] - 1])
    # print(self.place)
