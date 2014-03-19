#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Здесь внутри скобок содержится генератор.
Можно не указывать еще одни скобки.

"""


def main():
    open('data/output', 'w').writelines(
        line.replace('None', 'False')
        for line in open('data/input')
    )


if __name__ == '__main__':
    main()