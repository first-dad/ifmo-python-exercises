# -*- coding: utf-8 -*-


def urler(url):
    if type(url) != str:
        raise Exception('Url is not good')

    url = url.split('?')
    param = url[1].split('=')

    return int(param[1])