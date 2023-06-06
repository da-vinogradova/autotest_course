# Файл с фикстурами для всех тестов
import datetime
import pytest


@pytest.fixture(scope='class')
def setup_class():
    start_time = datetime.datetime.now()
    print('Время начала выполнения класса: ', start_time)
    yield start_time
    print('Время окончания выполнения класса: ', datetime.datetime.now() - start_time)


# @pytest.fixture()
# def teardown_class():
#     print('Время окончания выполнения класса: ', datetime.datetime.now())


@pytest.fixture()
def test_exec_time():
    """Фикстура, которая считает время выполнения теста"""
    start_time = datetime.datetime.now()
    yield start_time
    print("Время выполнения теста: ", datetime.datetime.now() - start_time)
