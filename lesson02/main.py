#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main():
    file_name = 'text'
    search_word = 'better'
    replace_word = 'worse'
    search_symbol = '.'
    template = '{0}'
    words_counter = 0
    symbols_counter = 0
    new_text = ''

    _file = open(file_name, 'r')

    for line in _file.readlines():
        new_text += line.replace(search_word, template)

        if line.rstrip().endswith(search_symbol):
            symbols_counter += 1

        words_counter += line.count(search_word)

    _file.close()

    print 'Количество слов "%s" в тексте: %d' % (search_word, words_counter)
    print 'Количество символов "%s" в тексте: %d\n' % (search_symbol, symbols_counter)
    print 'Новый текст:\n%s' % new_text.format(replace_word)


if __name__ == '__main__':
    main()
