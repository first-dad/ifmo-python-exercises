# -*- coding: utf-8 -*-


"""
xrange() создает генератор
"""


def main():
    name = 'Дмитрий'
    counter = 0

    while counter < 5:
        input_name = input('Введите ваше имя:\n')

        if len(input_name) > len(name):
            print('Поздравляем, %s!' % input_name)
            break
        else:
            counter += 1


if __name__ == '__main__':
    main()