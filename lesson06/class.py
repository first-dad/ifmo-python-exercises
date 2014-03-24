#!/usr/bin/python -tt
# coding: utf-8


class Bird:

    def __init__(self):
        pass

    def fly(self):
        print self, 'летит'

    def __str__(self):
        return 'Птица'


# Одиночное наследование
class Duck(Bird):
    pass


# Множественное наследование
class Goose(Duck, Bird):
    pass


if __name__ == '__main__':
    bird = Bird()
    bird.fly()

    # Duck является субклассом Bird
    print issubclass(Duck, Bird)