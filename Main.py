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
    data = dict()
    data['year'] = input('Введите год выпуска автомобиля:')
    data['model'] = input('Введите модель автомобиля:')
    data['producer'] = input('Введите производителя:')
    data['body_type'] = input('Введите тип кузова:')

    return lst.append(Car(year=data['year'], model=data['model'],
                          producer=data['producer'], body_type=data['body_type']))


def read():
    """ Reading from the file. """
    lst = []
    with open('data.dot') as f:
        for line in f.readlines():
            data = json.loads(line)
            lst.append(Car(year=data['year'], model=data['model'],
                           producer=data['producer'], body_type=data['body_type']))

    return lst


def write(lst):
    """ Writing to the file. """
    with open('data.dot', 'w') as f:
        for elem in lst:
            print(json.dumps(elem.__dict__), file=f)


def show(lst):
    """ Print objects. """
    # TODO


def main():
    """ Main function. """
    # TODO


if __name__ == '__main__':
    main()
