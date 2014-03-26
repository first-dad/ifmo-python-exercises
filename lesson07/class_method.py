#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from time import localtime


class Date(object):
    def __init__(self, value):
        self.value = value

    @classmethod
    def now(cls):
        return cls(localtime())


class EuroDate(Date):
    def __str__(self):
        return '%d-%d-%d' % (self.value.tm_year,
                             self.value.tm_mon,
                             self.value.tm_mday)


if __name__ == '__main__':
    local_time = localtime()

    date = Date(local_time)
    print date
    print date.now()

    euro_date = EuroDate(local_time)
    print euro_date
    print EuroDate.now()