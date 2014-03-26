#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import weakref


class A:
    def __init__(self):
        pass


class B(object):
    def __init__(self):
        pass

    def set(self, value):
        self.value = weakref.ref(value)


if __name__ == '__main__':
    a = A()
    b = B()
    b.set(a)
    print b.value
    del a
    print b.value