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

    def attack(self, characters: list, review: dict):
        damage = random.randint(0, self._attack)
        for character in characters:
            for key, value in review.items():
                if key != 'cp' and review[key] == character.place:
                    return character._get_damage(damage)
        return None


    def _get_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._sign = '-'
        return self

    def _move_side(self, field, pos_cur, pos_new):
        if 0 <= pos_new[0] <= field.size -1 and 0 <= pos_new[1] <= field.size -1:
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
