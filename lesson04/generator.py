#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Пройтись по папке с файлами.
В файле с расширением txt посчитать кол-во
слов python в строке

"""


from os import listdir


def generator():
    dir_name = 'data'
    ext_name = 'txt'
    search_word = 'better'

    for file_name in listdir(dir_name):
        if file_name.split('.')[-1] == ext_name:
            _file = open('%s/%s' % (dir_name, file_name), 'r')

            lines = _file.readlines()

            print 'Кол-во слов "%s" в файле %s:' % (search_word, file_name)

            for line in lines:
                amount = line.count(search_word)

                if amount > 0:
                    yield 'строка %2d: %d' % (lines.index(line) + 1, amount)

            _file.close()


if __name__ == '__main__':
    for output in generator():
        print output