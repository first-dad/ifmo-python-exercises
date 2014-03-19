#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Генератор в одну строку

"""


from os import listdir


def main():
    generator = (
        line.count('better') for _file in listdir('data')
        for line in open('data/' + _file)
        if '.txt' in _file
        if 'better' in line
    )

    for output in generator:
        print output


if __name__ == '__main__':
    main()