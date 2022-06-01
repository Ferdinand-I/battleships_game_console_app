from constants import ROWS_DICT
from core import get_key


class Pole:
    """Class that represents the Pole model."""
    # Constants for pole fields.
    empty_field = [0]
    ship_field = [4]
    dead_field = [2]
    pole: dict = None

    def __init__(self, name: str, size=10):
        self.name = name
        self.size = size

    def create(self):
        """Create an empty pole."""
        pole = {'a': [], 'b': [], 'c': [], 'd': [],
                'e': [], 'f': [], 'g': [], 'h': [],
                'i': [], 'j': []}
        for row in pole:
            for field in range(self.size):
                pole[row].append(self.empty_field)
        self.pole = pole
        return self.pole

    def get_field_value(self, coordinates: tuple):
        """Method that gets field of pole via coordinates."""
        if (
                coordinates[0] in ROWS_DICT.values()
                and coordinates[1] in ROWS_DICT.keys()
        ):
            return self.pole[coordinates[0]][coordinates[1] - 1]

    def view_pole(self):
        """Shows a pole in pretty view."""
        if self.pole:
            print(f'\n{self.name}', end='\n\n')
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
            print('\nMiss!')
            self.view_pole()
        elif field == self.dead_field:
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

    def __init__(self, pole: Pole, length: int, vector: str, point: tuple):
        self.length = length
        self.pole = pole
        self.vector = vector
        self.point = point

    def place(self):
        """Place ship on pole matrix."""
        pole = self.pole.pole
        row = pole[self.point[0]]
        coloumn = self.point[1] - 1
        if self.vector == 'right':
            for i in range(self.length):
                row[coloumn] = self.pole.ship_field
                coloumn += 1
            self.pole.view_pole()
        if self.vector == 'down':
            first_key = get_key(ROWS_DICT, self.point[0])
            for i in range(self.length):
                key = ROWS_DICT[first_key]
                pole[key][coloumn] = self.pole.ship_field
                first_key += 1
            self.pole.view_pole()

    def show_stats(self):
        """Show ship stats."""
        print(
            '\nHere are the stats of the ship you have chosen:\n'
            f'Pole: {self.pole}',
            f'Length: {self.length}',
            f'Direction: {self.vector}',
            f'Start point: {self.point}\n',
            sep='\n'
        )
