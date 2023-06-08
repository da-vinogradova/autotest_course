# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("a, b, result", [pytest.param(16, 4, 4, marks=pytest.mark.smoke),
                                          (10, 1.6, 6.25),
                                          (-7, 1, -7),
                                          (0, 4, 0),
                                          pytest.param(5, 0, 0, marks=pytest.mark.skip("Потому что тест по должен падать"))])
def test_all(a, b, result):
    assert all_division(a, b) == result
