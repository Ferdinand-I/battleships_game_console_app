""""Module that provides cores for whole project."""
from constants import DEFAULT_PREFIX, COLORED_RED_PREFIX
import models
import re


def validate_name(name: str) -> bool:
    return (
            re.match(pattern=r'^\s+$', string=name) or
            re.match(pattern=r'^\d+$', string=name) or
            name == ''
    )


def unpack_ships_init(pole, lst, **kwargs):
    """Helps unpacking ship objects with recieved data."""
    message = (f'{COLORED_RED_PREFIX}Check the settings, '
               f'data is broken!' + DEFAULT_PREFIX)
    keys = ['single_deck', 'double_deck', 'triple_deck', 'quadrupel']
    if kwargs.get(keys[0]):
        length_single = kwargs.get(keys[0])[0]
        count = kwargs.get(keys[0])[1]
        for i in range(count):
            lst.append(models.Ship(pole=pole, length=length_single))
    else:
        print(message)
    if kwargs.get(keys[1]):
        length_double = kwargs.get(keys[1])[0]
        count = kwargs.get(keys[1])[1]
        for i in range(count):
            lst.append(models.Ship(pole=pole, length=length_double))
    else:
        print(message)
    if kwargs.get(keys[2]):
        length_triple = kwargs.get(keys[2])[0]
        count = kwargs.get(keys[2])[1]
        for i in range(count):
            lst.append(models.Ship(pole=pole, length=length_triple))
    else:
        print(message)
    if kwargs.get(keys[3]):
        length_quadrupel = kwargs.get(keys[3])[0]
        count = kwargs.get(keys[3])[1]
        for i in range(count):
            lst.append(models.Ship(pole=pole, length=length_quadrupel))
    else:
        print(message)


def get_key(dictionary: dict, value):
    """Allow to recieve the dictionary key by value."""
    for key, val in dictionary.items():
        if val == value:
            return key


def blue_wrapper(func):
    """Do pretty view."""
    def wrap(*args):
        blue_separator = (
                '\n\33[34m----------------------------------------------------'
                + DEFAULT_PREFIX
        )
        print(blue_separator)
        func(*args)
        print(blue_separator)
    return wrap
