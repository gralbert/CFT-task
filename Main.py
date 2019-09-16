"""
Auto catalogue.
Developed by Grigorev Albert.
"""

from CarClass import Car
import json


def accept_command():
    """ Asks for the command number. """
    while True:
        command = input('Введите номер команды: ')
        try:
            command = int(command)
        except TypeError:
            pass

        if command in [1, 2, 3, 4, 5]:
            return command
        else:
            print('Ошибка ввода')


def add(lst):
    """ Asks user about the car. """
    # TODO


def read():
    """ Reading from the file. """
    # TODO


def write(lst):
    """ Writing to the file. """
    # TODO


def show(lst):
    """ Print objects. """
    # TODO


def main():
    """ Main function. """
    # TODO


if __name__ == '__main__':
    main()
