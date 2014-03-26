#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Static:
    def __init__(self):
        pass

    @staticmethod
    def fn():
        print 'This is static method!'


if __name__ == '__main__':
    Static.fn()