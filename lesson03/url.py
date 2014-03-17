#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import urllib


def page(url):
    def get(url):
        return urllib.urlopen(url).read()

    return get(url)


print page('http://ya.ru/')
print
print page('http://google.com/')