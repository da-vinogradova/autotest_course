# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    Функция перевода арабских цифр в риские
    :param val: int арабское число
    :return: str римское число
    """
    # Список для перевода
    list_roma_num = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M',)]
    roman_str = ''
    # Максимальное количество разрядов
    num_len = len(str(val)) - 1

    while val > 0:
        # выделяем первую цифру, которую сейчас будем переводить
        number = val // 10**num_len
        # остаток, который продолжим делить
        val = val % 10**num_len
        if number < 4:
            # напишем первое число из словаря number раз и добавим то, что уже написано
            roman_str += list_roma_num[num_len][0] * number
        elif number == 4:
            roman_str += list_roma_num[num_len][0] + list_roma_num[num_len][1]
        elif 5 <= number < 9:
            roman_str += list_roma_num[num_len][1] + list_roma_num[num_len][0] * (number - 5)
        else:
            roman_str += list_roma_num[num_len][0] + list_roma_num[num_len + 1][0]
        num_len -= 1

    print(roman_str)
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
