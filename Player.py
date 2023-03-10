from Character import Character


class Player(Character):

    def __init__(self, name):
        self._base_hp = 100
        self._hp = self._base_hp
        self._name = name
        self._attack = 10
        self._sign = "X"
        super().__init__(self)
