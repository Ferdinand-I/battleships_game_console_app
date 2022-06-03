"""Welcome to the 'Battleship' game.

Here are the rules:
...

Enjoy your expirience!
"""

from constants import (ROWS_DICT, COLORED_RED_PREFIX,
                       COLORED_GREEN_PREFIX, COLORED_BLACK_PREFIX,
                       COLORED_YELLOW_PREFIX)
from core import get_key, blue_wrapper
from game_settings import POLE_SIZE


class Pole:
    """Class that represents the Pole model."""
    # Constants for colored pole fields
    empty_field = f'{COLORED_BLACK_PREFIX}{[0]}'
    ship_field = f'{COLORED_GREEN_PREFIX}{[4]}'
    dead_field = f'{COLORED_RED_PREFIX}{[2]}'
    miss_field = f'{COLORED_YELLOW_PREFIX}{[0]}'
    pole: dict = None

    def __init__(self, name: str = 'Default name', size=POLE_SIZE):
        self.name = name
        self.size = size

    def create_pole(self):
        """Create an empty pole."""
        pole = {
            'a': [], 'b': [], 'c': [], 'd': [], 'e': [],
            'f': [], 'g': [], 'h': [], 'i': [], 'j': []
        }
        for row in pole:
            for field in range(self.size):
                pole[row].append(self.empty_field)
        self.pole = pole
        self.view_pole()

    def get_field_value(self, coordinates: tuple):
        """Method that gets field of pole via coordinates."""
        if (
                coordinates[0] in ROWS_DICT.values()
                and coordinates[1] in ROWS_DICT.keys()
        ):
            return self.pole[coordinates[0]][coordinates[1] - 1]

    @blue_wrapper
    def view_pole(self):
        """Shows a pole in pretty view."""
        if self.pole:
            print(f'\nHere is {self.name}:', end='\n\n')
            for row in self.pole:
                print(*self.pole[row], end='\n',)
        else:
            print("\nCreate pole first!\n")

    def shoot(self, coordinates: tuple):
        """Method that allows you to shoot on fields
        and if succeeded change damaged field with a dead flag.
        """
        field = self.get_field_value(coordinates)
        if field == self.empty_field:
            self.pole[coordinates[0]][coordinates[1] - 1] = self.miss_field
            print('\nMiss!')
            self.view_pole()
        elif field == (self.dead_field or self.miss_field):
            print('\nYou already got it, try another field to shoot on!')
            self.view_pole()
        else:
            self.pole[coordinates[0]][coordinates[1] - 1] = self.dead_field
            print(f'\nYou got it!')
            self.view_pole()

    def __str__(self) -> str:
        return self.name


class Ship:
    """Class that represents the Ship model."""
    point = None
    vector = None
    __placed = False
    damaged_fields: list = list()

    def __init__(self, **kwargs):
        """Creates ship object that binded with Pole."""
        if kwargs.get('length') and kwargs.get('pole'):
            self.length = kwargs['length']
            self.pole = kwargs['pole']

    def place_ship(self, **kwargs):
        """Place ship on pole matrix."""
        pole = self.pole.pole
        if self.__placed:
            print('\nThis ship is already placed.')
            return None
        if kwargs.get('point') and kwargs.get('vector'):
            self.__placed = True
            self.point = kwargs['point']
            self.vector = kwargs['vector']
            row = pole[self.point[0]]
            coloumn = self.point[1] - 1
            if self.vector == 'right':
                for i in range(self.length):
                    row[coloumn] = self.pole.ship_field
                    coloumn += 1
                row[coloumn] = self.pole.empty_field
                self.pole.view_pole()
            if self.vector == 'down':
                first_key = get_key(ROWS_DICT, self.point[0])
                for i in range(self.length):
                    key = ROWS_DICT[first_key]
                    pole[key][coloumn] = self.pole.ship_field
                    first_key += 1
                self.pole.view_pole()
        else:
            print('\nCheck the point and vector arguments you have given.')

    @blue_wrapper
    def show_stats(self):
        """Show ship stats."""
        print(
            '\nHere are the stats of the ship you have chosen:\n'
            f'Pole: {self.pole}',
            f'Length: {self.length}',
            f'Direction: {self.vector}',
            f'Start point: {self.point}',
            f'Damaged fields: {None}\n',
            sep='\n'
        )
