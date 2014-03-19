#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""
С помощью генератора списков
сформировать список,
в котором расположены элементы с y > 20.

Сделать вывод с помощью функции join.
"""


def main():
    elements = [
        ('A', 1, 17, -9),
        ('B', 7, 38, 16),
        ('C', 12, 23, 8)
    ]

    lst = [element for element in elements if element[2] > 20]

    print ' '.join(str(el) for el in lst)


if __name__ == '__main__':
    main()
