# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

class RomanNums:
    def __init__(self, number):
        self.number = number

    def from_roman(self):
        """
        переводит римскую запись числа в арабскую
        """
        arab_num = 0
        dict_arab_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rome_num_len = len(self.number)
        i = 1
        while 0 < i < rome_num_len:
                # Нужно взять текущую и следующую цифру и посмотреть, что ключа у следующей цифры в словаре меньше
                # тогда можем смело писать текущую цифру
                if int(dict_arab_num.get(self.number[i - 1])) >= int(dict_arab_num.get(self.number[i])):
                        arab_num += dict_arab_num.get(self.number[i - 1])
                if int(dict_arab_num.get(self.number[i - 1])) < int(dict_arab_num.get(self.number[i])):
                        arab_num += (int(dict_arab_num.get(self.number[i])) - int(dict_arab_num.get(self.number[i - 1])))
                        arab_num -= int(dict_arab_num.get(self.number[i]))
                # Увеличение счетчика
                i += 1

        # Эта строчка нужна для обработки ситуации, когда остается последняя цифра. Либо изначально была единственная
        arab_num += dict_arab_num.get(self.number[-1])

        return arab_num

    def is_palindrome(self):
        """
        метод определяет, является ли арабское число палиндромом (True - является, иначе False)
        т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
        :return:
        """
        str_arab_num = str(self.from_roman())
        is_polindrome = True
        # Найдем середину отрезка
        mediana = round(len(str_arab_num) / 2)
        i = 0
        while mediana > 0 and is_polindrome:
            if str_arab_num[i] != str_arab_num[-(i+1)]:
                is_polindrome = False
            i += 1
            mediana -= 1
        print(is_polindrome)
        return is_polindrome


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]

test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
