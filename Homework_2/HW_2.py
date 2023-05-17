import math

# Задание 2
# ax^2+bx+c=0. Дискриминант > 0. Найти корни и округлить до 2-х знаков после запятой
a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))

# Дискриминант
d = float(math.pow(b, 2) - 4 * a * c)

# корень 1 и 2
root_1 = round((-b + math.sqrt(d)) / (2 * a), 2)
root_2 = round((-b - math.sqrt(d)) / (2 * a), 2)

print("Корень 1: " + str(root_1) + " " + "Корень 2: " + str(root_2))
