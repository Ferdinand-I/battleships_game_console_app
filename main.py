import models


def main():
    input('Press Enter to start the game')
    user_name = input('Input your name below: \n')
    pole = models.Pole(name=f'{user_name} Pole')
    pole.create()
    pole.view_pole()


if __name__ == '__main__':
    main()
