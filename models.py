ROWS_DICT = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
    6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'
}


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


class Pole:
    """Class that represents the Pole model."""
    empty_field = [0]
    ship_field = [4]
    dead_field = [2]
    pole = None

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

    def view_pole(self):
        """Shows a pole in pretty view."""
        if self.pole:
            print(f'\n{self.name}', end='\n\n')
            for row in self.pole:
                print(*self.pole[row], end='\n',)
        else:
            print("\nCreate pole first!\n")

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

    def show(self):
        """Show ship stats."""
        print(
            '\nHere are the stats of the ship you have chosen:\n'
            f'Pole: {self.pole}',
            f'Length: {self.length}',
            f'Direction: {self.vector}',
            f'Start point: {self.point}\n',
            sep='\n'
        )
