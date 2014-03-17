#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from sys import setrecursionlimit, getrecursionlimit


def factorial(n):
    """
    Текст документации

    >>> factorial(100)
    3628800
    >>>
    """

    setrecursionlimit(1000)

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    num = 10

    print 'Factorial of %d: %d' % (num, factorial(num))
    print
    print 'Recursion limit: %d' % getrecursionlimit()
    print
    print help(factorial)
