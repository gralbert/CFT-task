"""
Auto catalogue.
Developed by Grigorev Albert.
"""

from CarClass import Car
import json
import random


def accept_command():
    """ Asks for the command number. """
    while True:
        command = input('Введите номер команды: ').replace(' ', '').replace('.', '')
        try:
            command = int(command)
        except ValueError:
            pass

        if command in [1, 2, 3, 4, 5]:
            return command
        else:
            print('Ошибка ввода')


def add(lst):
    """ Asks user about the car. """
    data = dict()
    while True:
        data['_producer'] = input('Введите производителя:')
        if len(data['_producer']) > 16:
            print('Длинновато! Постарайтесь сократить.')
        else:
            break

    while True:
        data['_model'] = input('Введите модель автомобиля:')
        if len(data['_producer']) > 14:
            print('Длинновато! Постарайтесь сократить.')
        else:
            break

    while True:
        data['_year'] = input('Введите год выпуска автомобиля:')
        if len(data['_producer']) > 4:
            print('Длинновато! Постарайтесь сократить.')
        else:
            break

    while True:
        data['_body_type'] = input('Введите тип кузова:')
        if len(data['_producer']) > 14:
            print('Длинновато! Постарайтесь сократить.')
        else:
            break

    # Generate auto's id.
    set_of_ids = set()
    for obj in lst:
        set_of_ids.add(obj.aid)

    data['_aid'] = random.randint(1000, 9999)
    while data['_aid'] in set_of_ids:
        data['_aid'] = random.randint(1000, 9999)

    return lst.append(Car(data))


def delete(lst):
    """ Delete car from the list. """
    try:
        aid = int(input('Введите ID автомобиля для удаления: '))
    except ValueError:
        print('\nID указан неверно.\n')
        return lst

    for num in range(len(lst)):
        if lst[num].aid == aid:
            lst.pop(num)
            print('Успешно удалено.\n')
            return lst
    print('\nID указан неверно. Повторите попытку. \n')
    return lst


def read():
    """ Reading from the file. """
    lst = []
    try:
        with open('data.dot') as f:
            for line in f.readlines():
                data = json.loads(line)
                lst.append(Car(data))

    except FileNotFoundError:
        print('Внимание! Файл с данными не найден. Создан новый. \n')
        with open('data.dot', 'w') as f:
            print('', file=f, end='')

    return lst


def write(lst):
    """ Writing to the file. """
    with open('data.dot', 'w') as f:
        for elem in lst:
            print(json.dumps(elem.__dict__), file=f)


def show(lst):
    """ Print objects. """
    header = '|{:^8}|{:^12}|{:^18}|{:^16}|{:^16}|'.format('ID', 'Год', 'Производитель',
                                                          'Модель', 'Тип кузова')
    print(header)
    for elem in lst:
        print(elem)


def edit(lst):
    """ Edit information about car. """
    try:
        aid = int(input('Введите ID автомобиля для редактирования: '))
    except ValueError:
        print('\nID указан неверно.\n')
        return lst

    print('Что редактируем? \n'
          '1. Производитель \n'
          '2. Модель \n'
          '3. Год выпуска \n'
          '4. Тип кузова \n')

    try:
        cmd = int(input('Введите номер: ').replace(' ', '').replace('.', ''))
    except ValueError:
        print('\nНомер указан неверно.\n')
        return lst

    new_value = input('Введите новое значение: ')

    for num in range(len(lst)):
        if lst[num].aid == aid:
            if cmd == 1:
                lst[num].producer = new_value
                return lst
            elif cmd == 2:
                lst[num].model = new_value
                return lst
            elif cmd == 3:
                lst[num].year = new_value
                return lst
            elif cmd == 4:
                lst[num].body_type = new_value
                return lst
            print('\nНомер указан неверно. Повторите попытку. \n')
            return lst
    print('\nID указан неверно. Повторите попытку. \n')
    return lst


def main():
    """ Main function. """
    lst = read()
    while True:
        print('1. Просмотреть информацию об автомобилях. \n'
              '2. Добавить новый автомобиль. \n'
              '3. Удалить автомобиль из списка. \n'
              '4. Редактировать информацию об автомобиле. \n'
              '5. Выход.')
        command = accept_command()

        if command == 1:
            show(lst)
        elif command == 2:
            add(lst)
            write(lst)
        elif command == 3:
            lst = delete(lst)
            write(lst)
        elif command == 4:
            edit(lst)
            write(lst)
        else:
            break

    print('Спасибо за визит!')


if __name__ == '__main__':
    main()
