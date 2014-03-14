#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main():
    y_axis = []
    elements = [
        ('A', 1, 17, -9),
        ('B', 7, 38, 16),
        ('C', 12, 7, 8)
    ]

    for element in elements:
        y_axis.append(element[2])

    for element in elements:
        if elements.index(element) == y_axis.index(max(y_axis)):
            print('%s: %2d, %2d, %2d -> UPPER' % element)
        else:
            print('%s: %2d, %2d, %2d' % element)


if __name__ == '__main__':
    main()

