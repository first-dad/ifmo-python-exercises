#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class A(object):
    # Другие атрибуты и методы устанавливать уже нельзя
    __slots__ = ('name', 'age')

    def __init__(self):
        pass

if __name__ == '__main__':
    a = A()

    print a.test