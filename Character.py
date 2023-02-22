import random


class Character:

    @property
    def name(self) -> int:
        return self._name

    @property
    def full_hp(self) -> int:
        return self._base_hp

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def attack(self) -> int:
        return self._attack

    def __init__(self, character) -> None:
        self._name = character._name
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
