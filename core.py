""""Module that provides cores for whole project."""


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
