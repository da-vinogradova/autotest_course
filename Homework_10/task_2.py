# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_div_int():
    assert all_division(16, 4, 2, 1) == 2

@pytest.mark.without_zero
def test_div_double():
    assert all_division(10, 1.6) == 6.25

@pytest.mark.smoke
def test_negative():
    assert all_division(-7, 1) == -7


@pytest.mark.with_zero
def test_zero_div():
    assert all_division(0, 4) == 0

@pytest.mark.with_zero
def test_div_zero():
    # Указали, что в результате выполнения теста должно упасть исключение
    with pytest.raises(ZeroDivisionError):
        all_division(5, 0)

