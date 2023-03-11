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
        self._step = character._step
        self._place = None

    def attack(self, character):
        damage = random.randint(0, self._attack)
        character.__get_damage(damage)

    def __get_damage(self, damage):
        self._hp -= damage

    def move_side(self, field, x_cur, y_cur, x_new, y_new):
        field.field[x_cur][y_cur] = '-'
        field.field[x_new][y_new] = self._sign
        self._place = [x_new, y_new]
        return field

    def move(self, field, move):
        step = self._step
        x_cur, y_cur = self._place
        x_new = x_cur
        y_new = y_cur
        match move:
            case Move.LEFT.value:
                return self.move_side(field, x_cur, y_cur, x_new, y_new - step)
            case Move.DOWN.value:
                return self.move_side(field, x_cur, y_cur, x_new + step, y_new)
            case Move.UP.value:
                return self.move_side(field, x_cur, y_cur, x_new - step, y_new)
            case Move.RIGHT.value:
                return self.move_side(field, x_cur, y_cur, x_new, y_new + step)
            
