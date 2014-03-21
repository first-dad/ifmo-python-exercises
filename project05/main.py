#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from sys import argv
from os import system
from mvc.htmler import htmler
from mvc.urler import urler
from mvc.sqler import sqler


if __name__ == '__main__':
    if len(argv) < 2:
        url = raw_input('Type url to parse:\n')
    else:
        url = argv[1]

    try:
        params = urler(url)
        data = sqler(params)
        page = htmler(data)

        open('index.html', 'w').write(page)

        system('google-chrome index.html')
    except:
        raise Exception("Can't perform operation")
