import pytest


# Это фикстуры для x-unit-style
def setup_module():
    """Модуль выполняется ОДИН раз ПЕРЕД набором тестов"""
    pass


def setup_function():
    """Функция выполняется КАЖДЫЙ раз ПЕРЕД запуском какого-либо теста"""
    pass


def teardown_function():
    """Функция выполняется КАЖДЫЙ раз ПОСЛЕ запуском какого-либо теста.
    Она может не вызываться, если не выполнился setup_module"""
    pass


def teardown_module():
    """Модуль выполняется ОДИН раз ПОСЛЕ набором тестов.
    Она может не вызываться, если не выполнился setup_module"""
    pass


# Фикстуры для класса называются по-другому
class Test:

    @classmethod
    def setup_class(cls):
        """Выполняется 1 раз перед"""
        pass

    @classmethod
    def teardown_class(cls):
        """Выполняется один раз после"""
        pass

    @classmethod
    def setup_method(self):
        """Выполняется 1 раз перед"""
        pass

    @classmethod
    def teardown_method(self):
        """Выполняется один раз после"""
        pass

    # В Pytest фикстура обозначается декоратором @pytest.fixture()