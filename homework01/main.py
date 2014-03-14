#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""
Задание:

Создать папку.
В папку записать файлы разных форматов xls, doc, txt, mp3 и т.д.
Создать программу, которая будет смотреть эту папку, перечислением проходить по всем файлам
и если встречает в какой-то момент файл txt, то она его открывает и ищет в нем слово python.
Выдает кол-во слов python в файле.
"""


from os import listdir


def count_words(search_word, text):
    search_word = search_word.lower()
    counter = 0

    for line in text:
        words = line.split()

        for word in words:
            index = word.lower().find(search_word)

            if index > -1:
                counter += 1

    return counter


def main():
    dir_name = 'data'
    ext_name = 'txt'
    search_word = 'python'

    for file_name in listdir(dir_name):
        if file_name.split('.')[-1] == ext_name:
            _file = open('%s/%s' % (dir_name, file_name), 'r')

            num_of_words = count_words(search_word, _file)

            print 'Кол-во слов "%s" в файле %s: %d' % (search_word, file_name, num_of_words)

            _file.close()


if __name__ == '__main__':
    main()
