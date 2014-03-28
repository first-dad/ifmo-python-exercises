#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from datetime import datetime


def decor(fn):
    """
    Декоратор оборачивает функцию, т.е.
    можно изменить поведение функции или добавить
    что-нибудь в начало или конец.
    """
    def new():
        print datetime.now()
        fn()
        print datetime.now()

    return new


@decor
def counter():
    num = 10000000

    while num > 0:
        num -= 1

if __name__ == '__main__':
    counter()