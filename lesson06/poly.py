#!/usr/bin/python -ttget_color
# -*- coding: utf-8 -*-


def processor(reader, converter, writer):
    """
    Полиморфизм
    Writer и Reader могут быть файлами
    """
    while True:
        data = reader.read()

        if not data:
            break

        data = converter(data)
        writer.write(data)


if __name__ == '__main__':
    pass
