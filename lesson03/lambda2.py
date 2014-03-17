#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main():
    f = lambda a, b, c: [0, b + c][a == 'plus']
    print f('plus', 2, 3)


if __name__ == '__main__':
    main()