import models
from core import unpack_ships_init
from game_settings import SETTINGS

pole = models.Pole(name='Pole one')
pole.create_pole()
lst = list()
ship = models.Ship(length=4, pole=pole)
ship.place_ship(vector='right', point=('a', 5))

data = SETTINGS.get('ships_count')
unpack_ships_init(pole, lst, **data)
print(len(lst))
print(data)