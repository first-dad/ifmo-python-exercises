#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from datetime import datetime


def model(cls, time):
    print time

    if hasattr(cls, 'model'):
        return cls

    class New(cls):
        model = 'Nissan'

    return New


@model(datetime.now())
class Auto:
    model = 'BMW'

    def __init__(self):
        pass


if __name__ == '__main__':
    print Auto.model
