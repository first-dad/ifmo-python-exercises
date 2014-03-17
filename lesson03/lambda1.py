#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main():
    x = lambda *lst: [n*n for n in lst]
    print x(1, 2, 3)


if __name__ == '__main__':
    main()