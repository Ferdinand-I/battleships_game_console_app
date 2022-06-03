import models
from constants import (COLORED_BLACK_PREFIX,
                       ITALICS_PREFIX, DEFAULT_PREFIX)
from core import unpack_ships_init, validate_name
from game_settings import ERROR_MESSAGES, SETTINGS


def main():
    """Main logic of the game."""
    print(f'{ITALICS_PREFIX}{models.__doc__}{DEFAULT_PREFIX}')
    input('Press Enter to start the game')
    while True:
        first_user = input('\nInput the name of the first player below: \n')
        if validate_name(first_user):
            print(ERROR_MESSAGES.get('name_validation') + COLORED_BLACK_PREFIX)
            continue
        else:
            break
    pole = models.Pole(name=f'{first_user} Pole')
    pole.create_pole()
    while True:
        second_user = input('\nInput the name of the second player below: \n')
        if validate_name(second_user):
            print(ERROR_MESSAGES.get('name_validation') + COLORED_BLACK_PREFIX)
            continue
        else:
            break
    pole_2 = models.Pole(name=f'{second_user} Pole')
    pole_2.create_pole()
    first_user_ships = list()
    second_user_ships = list()
    unpack_ships_init(pole, first_user_ships, **SETTINGS.get('ships_count'))
    unpack_ships_init(pole_2, second_user_ships, **SETTINGS.get('ships_count'))
    print(f'{first_user}, for now place your ships carefully.\n')
    for i in range(len(first_user_ships)):
        coordinates = input('Place your ships with this format: '
                            '"a 1 right" \nWhere "a" and "1" are coordinates '
                            'realated to row and column accordingly,\nand '
                            '"right" is the direction. For example: \n'
                            'for 3-decks ship "a 1 right" means that ship '
                            'will be placed from "a1" field to the right \n'
                            'and will take "a1", "a2", "a3" fileds summary.\n'
                            )


if __name__ == '__main__':
    main()
