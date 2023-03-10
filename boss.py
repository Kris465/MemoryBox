# Реализовать класс - наследник от Mob. (моб - бос)
# НЕ переопределять получение урона.
# Создать два собственных уникальных метода.
# (Например, телепортацию и урон по окружающим клеткам)
from Mob import Mob


class Boss(Mob):

    def __init__(self, clothes, hat):
        super().__init__(clothes, hat)

    def teleport(self, field, move, player):
        super().move_type(field, move)
        super().attack(player)

    def circle_attack(self, field, player, mobs):
        list_character = mobs.copy()
        list_character.append(player)
        print(list_character)
        position = self.place
        for i in list_character:
            if field.field[position[0] - 1][position[1]] == i.sign:
                super().attack(player)
            if field.field[position[0] - 1][position[1]] == i.sign:
                super().attack(player)
            if field.field[position[0]][position[1] + 1] == i.sign:
                super().attack(player)
            if field.field[position[0]][position[1] - 1] == i.sign:
                super().attack(player)
