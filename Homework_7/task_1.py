# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False
import math


class Segment:

    def __init__(self, segm1, segm2):
        """
        Конструктор для класса Segment, который определяет отрезок
        :param segm1: координаты первой точки отрезка
        :param segm2: координаты второй точки отрезка
        """
        self.segm1 = segm1
        self.segm2 = segm2

    def length(self):
        """
        Метод возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
        """
        x1 = self.segm1[0]
        y1 = self.segm1[1]
        x2 = self.segm2[0]
        y2 = self.segm2[1]
        a = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
        return a

    def x_axis_intersection(self):
        """
        возвращает True, если отрезок пересекает ось абцисс, иначе False
        """
        y1 = self.segm1[1]
        y2 = self.segm2[1]
        # если координаты по разным сторонам от 0, то значит пересекают ось
        if (y1 >= 0 > y2) or (y2 >= 0 > y1):
            return True
        else:
            return False

    def y_axis_intersection(self):
        """
        возвращает True, если отрезок пересекает ось ординат, иначе False
        """
        x1 = self.segm1[0]
        x2 = self.segm2[0]
        # если координаты по разным сторонам от 0, то значит пересекают ось
        if (x1 >= 0 > x2) or (x2 >= 0 > x1):
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
