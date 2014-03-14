# -*- coding: utf-8 -*-


def main(*lst):
    s = 0

    for num in lst:
        s += num

    print(s)


if __name__ == '__main__':
    main(1, 2, 3, 45, 2)