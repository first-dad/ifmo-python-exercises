# -*- coding: utf-8 -*-


def htmler(data):
    if not data or type(data) != dict:
        raise Exception('Data is not good')

    template = open('template.tpl', 'r').read()
    books = ''

    for book in data['books']:
        books += '<li>%s</li>' % book

    return template.format(data['user_name'], books)

