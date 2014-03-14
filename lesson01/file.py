# -*- coding: utf-8 -*-


def open_file():
    file_name = input('Введите имя файла:\n')

    try:
        file = open(file_name, 'r')
    except IOError:
        print('Такого файла нет :(')
        return

    print(file.read())


open_file()