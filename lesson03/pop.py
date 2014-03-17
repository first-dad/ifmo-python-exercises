#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main(**params):
    if params:
        return params.pop('color', 'black')
    else:
        raise TypeError('Ошибка!')


if __name__ == '__main__':
    print main(color='white')
    print
    print main()