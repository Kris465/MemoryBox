from Field import Field
from Mob import Mob
from Player import Player
from controller import Controller
from viewConsole import ViewConsole

player = Player('lameR')
mobs = [Mob("Шляпа", "Платье") for _ in range(5)]
field = Field()
vc = ViewConsole()
controller = Controller(vc, player, mobs, field)
controller.init_units()
game = True
while game:
    controller.move()
