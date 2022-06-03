"""Local game settings."""
from constants import COLORED_RED_PREFIX


POLE_SIZE = 10

SETTINGS = {
    'ships_count': {
        'single_deck': (1, 4),
        'double_deck': (2, 3),
        'triple_deck': (3, 2),
        'quadrupel': (4, 1)
    }
}

ERROR_MESSAGES = {
    'name_validation': f'{COLORED_RED_PREFIX}Invalid username! '
                       'Username cannot contains only whitespaces '
                       'or only digits!'
}
