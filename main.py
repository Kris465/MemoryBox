from Field import Field
from Mob import Mob
from Player import Player
from characters import Characters
from controller import Controller
from viewconsole import ViewConsole

characters = Characters()
characters.add(Player('lameR'))
[characters.add(Mob("Шляпа", "Платье")) for _ in range(5)]
field = Field()
controller = Controller(characters, field)
vc = ViewConsole(controller)
vc.start()
