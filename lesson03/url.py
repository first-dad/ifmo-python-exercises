#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import urllib


def page(url):
    def get(url):
        return urllib.urlopen(url).read()

    return get(url)


if __name__ == '__main__':
    print page('http://ya.ru/')
    print
    print
    print page('http://google.com/')