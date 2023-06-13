# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time
from pathlib import Path


def func_log(func_to_decor):
    """Декоратор, который может принимать аргумент file_log (Путь до файла)"""

    def wrapper(file_log='log.txt'):
        """Декоратор, который может принимать аргумент file_log (Путь до файла)"""
        # Здесь перебиваем название декоратора и пишем именно функцию, которую вызываем. и также хелп
        wrapper.__name__ = func_to_decor.__name__
        wrapper.__doc__ = func_to_decor.__doc__

        # Строка, которая берет имя декорируемой функции и добавляет время ее вызова
        res = func_to_decor.__name__ + " вызвана " + datetime.datetime.now().strftime("%d.%m %H:%M:%S")
        func_to_decor(file_log)
        # Теперь нашу доработанную функцию надо записать в файл
        # Создаем относительный путь до файла с заданием. Из-за того, что не знаем слэши, разбиваем папки через запятую
        path = Path.cwd().joinpath(file_log)
        with open(path, 'a') as func_info:
            func_info.write(res)
        return res
    return wrapper

def my_file(file_log):
    """ Функция возвращает время, когда была вызвана в формате %d.%m %H:%M:%S"""
    time.sleep(3)
    # call_time = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
    # return call_time


f = func_log(my_file)
f()

# help, когда нет декоратора
help(my_file)
# help, когда есть декоратор
help(f)