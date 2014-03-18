#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""
Переводчик

Запускать через командную строку

./translate.py
выведет полное содержимое словаря

./translate.py run
слово, транскрипцию и значения во всех частях речи

./translate.py run -t verb
слово, транскрипция и значения
в указаной части речи после параметра -t

./translate.py run -l
слово и транслитерация
"""


from sys import argv
from json import load


units = None
speech_parts = {
    'verb': 'глагол',
    'noun': 'существительное',
    'adjective': 'прилагательное'
}


def display_all():
    print '*** Словарь ***'
    print
    for unit in units:
        print '~ %d ~' % (units.index(unit) + 1)
        print '%s [%s]' % (unit['word'].encode('utf-8'), unit['transliteration'].encode('utf-8'))
        print

        for speech_part in unit['meaning']:
            print '%s:' % speech_parts[speech_part]
            for meaning in unit['meaning'][speech_part]:
                print '- %s' % meaning.encode('utf-8')
            print

        print


def display_type(word, speech_part):
    for unit in units:
        if unit['word'].encode('utf-8') == word:
            print '%s [%s]' % (unit['word'].encode('utf-8'), unit['transliteration'].encode('utf-8'))
            print '%s:' % speech_parts[speech_part]
            for meaning in unit['meaning'][speech_part]:
                print '- %s' % meaning


def display_transliteration(word):
    for unit in units:
        if unit['word'].encode('utf-8') == word:
            print '%s [%s]' % (unit['word'].encode('utf-8'), unit['transliteration'].encode('utf-8'))


def display_word(word):
    for unit in units:
        if unit['word'].encode('utf-8') == word:
            print '%s [%s]' % (unit['word'].encode('utf-8'), unit['transliteration'].encode('utf-8'))
            print

            for speech_part in unit['meaning']:
                print '%s:' % speech_parts[speech_part]
                for meaning in unit['meaning'][speech_part]:
                    print '- %s' % meaning.encode('utf-8')
                print

            print


def main(options):
    dictionary = open('dictionary.json', 'r')
    global units
    units = load(dictionary)

    if len(options) == 0:
        display_all()
    elif len(options) == 1:
        display_word(options[0])
    else:
        for option in options[1:]:
            index = options.index(option) + 1

            if option == '-t':
                display_type(options[0], options[index])
            elif option == '-l':
                display_transliteration(options[0])

    dictionary.close()


if __name__ == '__main__':
    main(argv[1:])
