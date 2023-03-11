from random import randint


class Controller:
    def __init__(self, vc, player, mobs, field):
        self.characters = []
        self.review_attr = None
        self.view = vc
        self.player = player
        self.mobs = mobs
        self.field = field
        self.__display_info()


    def review(self):
        self.review_attr = self.player.review()
        self.move()

    def move(self):
        move = self.view.move()
        if move == 1:
            move_side = self.view.movement()
            self.field = self.player.move(self.field, move_side, self.review_attr)
            self.field_update()
        elif move == 2:
            character = self.player.attack(self.characters, self.review_attr)
            self.view.damage(character)
            self.field_update()
            [self.characters.remove(ch) for ch in self.characters if ch.hp <= 0]
        self.__display_info()

    def field_update(self):
        for character in self.characters:
            place = character.place
            self.field.field[place[0]][place[1]] = character.sign

    def __display_info(self):
        self.view.display_info(self.field)

    def ran(self):
        return randint(0, self.field.size - 1)

    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        self.player.place = self.generate()
        self.field.field[self.player.place[0]][self.player.place[1]] = self.player.sign
        for i in self.mobs:
            i.place = self.generate()
            self.field.field[i.place[0]][i.place[1]] = i.sign
        self.characters = [i for i in self.mobs]
        self.characters.append(self.player)
        self.__display_info()
