#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Meta(type):
    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            if key.startswith('__'):
                continue
            if not hasattr(value, '__call__'):
                continue
            if not getattr(value, '__doc__'):
                raise TypeError('%s must have doc-string' % key)

        type.__init__(self, name, bases, dict)


class A:
    __metaclass__ = Meta


class B(A):
    def __init__(self):
        pass

    def fn(self):
        """
        Документация
        """
        print 'test'


if __name__ == '__main__':
    """
    Тоже самое что:

    class Test(object):
        pass
    """
    class_name = 'Test'
    class_body = 'def go(self): return 1'
    class_dict = {}
    class_parents = (object,)

    exec(class_body, globals(), class_dict)

    Test = type(class_name, class_parents, class_dict)

    print Test().go()