#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Car:
    max_speed = 250

    def __init__(self, model='Lada'):
        self.model = model

    def drive(self, time):
        print 'Автомобиль %s проехал %f км' % (self.model, float(time) / 60 / 60 * self.max_speed)


if __name__ == '__main__':
    bmw = Car('BMW')
    bmw.drive(10)