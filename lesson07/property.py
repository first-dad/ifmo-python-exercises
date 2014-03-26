#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class A(object):
    __x = 1

    def __init__(self):
        pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @x.deleter
    def x(self):
        del self.__x


if __name__ == '__main__':
    a = A()
    print a.x
    a.x = 2
    print a.x
    del a.x
    print a.x