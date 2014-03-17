#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


def main(action, a, b):
    if action == 'minus':
        return a - b
    elif action == 'divide':
        return a / b
    elif action == 'multiply':
        return a * b


if __name__ == '__main__':
    main()