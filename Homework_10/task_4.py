# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

class Test:

    def test_first(self):
        print("Это первый тест")
        time.sleep(1)

    def test_second(self, test_exec_time):
        print("Это второй тест")
        time.sleep(1)

    def test_third(self, test_exec_time):
        print("Это третий тест")
        time.sleep(2)

    def test_fourth(self):
        print("Это четвертый тест")
        time.sleep(1)
