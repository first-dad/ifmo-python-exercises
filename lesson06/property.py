#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Car(object):
    _color = None
    cost = 3000

    def set_color(self, _color):
        self._color = _color
        self.cost -= 1000

    def get_color(self):
        return self._color

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color, 'This is color')


if __name__ == '__main__':
    bmw = Car()
    bmw.color = 'green'
    bmw.color = 'red'

    print bmw.cost
    print bmw.color