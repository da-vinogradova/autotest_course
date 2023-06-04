# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
from pathlib import Path

# получим путь до нужного файла
path = Path('test_file', 'task_3.txt')
# Получим абсолютный путь, соединив текущую директорию и нужный файл
abs_path = Path.cwd().joinpath(path)

# Используем контекстный менеджер
with open(abs_path, 'r') as fr:
    task3_text = fr.read()

    # разделим все по покупкам
    split_text = task3_text.split('\n\n')

    # список, в котором будет сумма всех покупок
    sum_list = []

    # для каждой покупки выделим цену товаров
    for el in split_text:
        split_purchase = el.split('\n')

        sum_num = 0
        # в каждой покупке найдем сумму товаров и запишем ее в в список
        for num in split_purchase:
            if num != '':
                sum_num += int(num)
        sum_list.append(sum_num)

    # Отсортируем стоимость покупок и сложим 3 максимальных
    three_most_expensive_purchases = 0
    for num in sorted(sum_list)[-3:]:
        three_most_expensive_purchases += num


# Здесь пишем код

assert three_most_expensive_purchases == 202346
