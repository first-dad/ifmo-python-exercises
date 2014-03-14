# -*- coding: utf-8 -*-


try:
    res = int(open('a.txt').read()) / int(open('b.txt').read())
    print(res)
except IOError:
    print('Один из файлов отсутствует')
except ZeroDivisionError:
    print('Деление на ноль')
except KeyboardInterrupt:
    print('Вызвано прерывание с клавиатуры')
except:
    print('Неизвестная ошибка')
finally:
    print('Конец')
