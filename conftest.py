# Файл с фикстурами для всех тестов
import datetime
import pytest


@pytest.fixture(scope='class')
def fixture_for_class():
    start_time = datetime.datetime.now()
    yield
    print('Время начала выполнения класса: ', start_time)
    end_time = datetime.datetime.now()
    print('\n','Время окончания выполнения класса: ', end_time)


@pytest.fixture()
def test_exec_time():
    """Фикстура, которая считает время выполнения теста"""
    start_time = datetime.datetime.now()
    yield start_time
    print("Время выполнения теста: ", datetime.datetime.now() - start_time)
