class Character:

    @property
    def name(self) -> int:
        return self.__name

    @property
    def full_hp(self) -> int:
        return self.__base_hp

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def attack(self) -> int:
        return self.__attack

    def __init__(self, name: str, hp: int, attack: int) -> None:
        self.__name = name
        self.__base_hp = hp
        self.__hp = self.__base_hp
        self.__attack = attack

