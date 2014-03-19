#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


"""

Сопрограмма может применяться
в асинхронном программировании

"""


def main(text):
    # если убрать while True, то придется после каждого
    # send делать next
    while True:
        print (yield) + text


if __name__ == '__main__':
    main = main('text')

    main.next()  # это обязательно перед send
    main.send(7)
    main.send('Hello!')
    main.send(18)
