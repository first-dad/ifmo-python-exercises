# -*- coding: utf-8 -*-


def urler(url):
    if type(url) != str:
        raise Exception('uri type must be string')

    url = url.split('?')
    param = url[1].split('=')

    return int(param[1])