#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class AttrDict(object):
    """
    What is it?
    """
    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass


if __name__ == '__main__':
    pass