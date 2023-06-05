# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    first_len = random.randint(1, 15)
    second_len = random.randint(1, 15)

    gen_str = ''
    while True:
        i = 1
        # Генерируем первое слово
        while i <= first_len:
            # 24 буквы в латинском алфавите
            gen_str += string.ascii_lowercase[random.randint(0, 24)]
            i += 1
        # Добавляем пробел
        gen_str += ' '
        # Генерируем второе слово
        i = 1
        while i <= second_len:
            # 24 буквы в латинском алфавите
            gen_str += string.ascii_lowercase[random.randint(0, 24)]
            i += 1

        yield gen_str


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
