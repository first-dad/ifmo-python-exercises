#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Singleton(object):
    def __new__(cls):
        return cls


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()

    print a is b