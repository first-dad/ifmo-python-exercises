#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Переводчик
----------

./translate.py
выведет весь словарь

./translate.py [слово]
слово, транскрипция и значения во всех частях речи

./translate.py [слово] -[v | n | a]
слово, транскрипция и значения в указаной части речи
-v - глагол
-т - существительное
-a - прилагательное

./translate.py [слово] -t
значение и транслитерация


Пример:
./translate.py run -v

run [ран]

глагол:
- бежать
- бегать

"""


from sys import argv
from json import load


units = None
speech_parts = {
    'verb': 'глагол',
    'noun': 'существительное',
    'adjective': 'прилагательное'
}
options_aliases = {
    '-v': 'verb',
    '-n': 'noun',
    '-a': 'adjective' 
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
            print
            print '%s:' % speech_parts[speech_part]
            for meaning in unit['meaning'][speech_part]:
                print '- %s' % meaning


def display_transliteration(word):
    for unit in units:
        if unit['word'].encode('utf-8') == word:
            print '%s [%s]' % (unit['word'].encode('utf-8'), unit['transliteration'].encode('utf-8'))


def display_unit(word):
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
        display_unit(options[0])
    else:
        for option in options[1:]:
            index = options.index(option) + 1

            if option in options_aliases:
                display_type(options[0], options_aliases[option])
            elif option == '-t':
                display_transliteration(options[0])

    dictionary.close()


if __name__ == '__main__':
    main(argv[1:])
