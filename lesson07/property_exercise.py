#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Test:
    a = 1

    def __init__(self):
        pass

    @property
    def b(self, b):
        self.__b = b

    @b.getter
    def b(self):
        if hasattr(self, '__b'):
            return self.__b
        else:
            raise Exception('Attribute "b" is not exist')

    @b.deleter
    def b(self):
        del self.__b


if __name__ == '__main__':
    test = Test()
    print test.a
    print test.b
    test.b = 2
    print test.b
    del test.b
    print test.b