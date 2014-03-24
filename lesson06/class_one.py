#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Car:
    fuel = None
    fuel_amount = 0

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def fill(self, fuel, amount):
        self.fuel = fuel
        self.fuel_amount = amount

    def test(self, speed):
        print 'Тип бензина: %s' % self.fuel.brand
        print 'Кол-во бензина: %.2f' % float(self.fuel_amount)
        print 'Время преодоления 100км: %.2f сек.' % float(self.max_speed / speed * self.fuel.efficiency)

    def drive(self, time):
        print 'Автомобиль %s проехал %.2f км' % (self.model, float(time) / 3600 * self.max_speed)


class Fuel:
    def __init__(self, brand='petrol', efficiency=0.95):
        self.efficiency = efficiency
        self.brand = brand


if __name__ == '__main__':
    fuel = Fuel('diesel', 0.34)

    bmw = Car('BMW', max_speed=100)
    bmw.fill(fuel, amount=10)
    bmw.test(speed=10)