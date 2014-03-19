#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Пример итератора

"""


def main():
    mother = {
        'name': 'Alice',
        'age': 50,
        'child': None
    }

    son = {
        'name': 'Dan',
        'age': 18,
        'parent': mother
    }

    mother['child'] = son

    for option in mother:
        print '%s: %s' % (option, mother[option])


if __name__ == '__main__':
    main()