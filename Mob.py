from Character import Character


class Mob(Character):
    
    def __init__(self):
        self._base_hp = 100
        self._hp = self._base_hp
        self._name = "Mob"
        self._attack = 10
        self._sign = "#"

        super().__init__(self)