#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from abc import abstractmethod, abstractproperty, ABCMeta


class A:
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self):
        pass

    @abstractproperty
    def prop(self):
        pass


class B(A):
    __test = 1

    def __init__(self):
        pass

    def method(self):
        print 'method called'

    @property
    def prop(self):
        return self.__test


if __name__ == '__main__':
    b = B()
    b.method()
    print b.prop