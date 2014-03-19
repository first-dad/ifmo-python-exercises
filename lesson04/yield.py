#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Генератор для поиска слова "python"
в файле

"""


def gen():
    for line in open('text', 'r'):
        if 'python' in line:
            yield line


if __name__ == '__main__':
    for output in gen():
        print output
