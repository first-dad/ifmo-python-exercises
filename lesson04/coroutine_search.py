#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Реализация поиска слова в файле txt
с помощью сопрограммы

"""


from os import listdir


dir_name = 'data'


# сопрограмма
def find_word():
    while True:
        file_name = (yield)
        search_word = 'better'

        _file = open('%s/%s' % (dir_name, file_name), 'r')

        lines = _file.readlines()

        print 'Кол-во слов "%s" в файле %s:' % (search_word, file_name)

        for line in lines:
            amount = line.count(search_word)

            if amount > 0:
                print 'строка %2d: %d' % (lines.index(line) + 1, amount)

        _file.close()


def enumerate_dir(target):
    ext_name = 'txt'

    for file_name in listdir(dir_name):
        if file_name.split('.')[-1] == ext_name:
            target.next()
            target.send(file_name)


if __name__ == '__main__':
    enumerate_dir(find_word())