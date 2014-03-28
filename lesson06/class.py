#!/usr/bin/python -tt
# coding: utf-8

yfgkasjfgl
class Bird:
    size = 'small'

    def __init__(self):
        pass

    def fly(self):
        print self, 'летит'

    def __str__(self):
        return 'Птица'


# Одиночное наследование
class Duck(Bird):
    pass


# Множественное наследование и переопределение
class Goose(Duck, Bird):
    def __init__(self):
        self.size = 'Big'

    # ф-ия переопределена
    def fly(self):
        print 'Гусь летит'


if __name__ == '__main__':
    bird = Bird()
    bird.fly()

    goose = Goose()
    goose.fly()

    # Duck является субклассом Bird
    print issubclass(Duck, Bird)
