# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
from pathlib import Path

# получим путь до нужного файла
path = Path('test_file', 'task_3.txt')
# Получим абсолютный путь, соединив текущую директорию и нужный файл
abs_path = Path.cwd().joinpath(path)

# Откроем файл и вычитаем данные
task_3_file = open(abs_path)
task3_text = task_3_file.read()
# оставим только значения, которые в дальнейшем отсортируем
split_text = task3_text.split('\n')

# Удалим пустые
i = 0
while i < len(split_text):
    if split_text[i] == '':
        split_text.pop(i)
    i += 1

# Перегоним значения в инт
for c, el in enumerate(split_text):
    if el != '':
        split_text[c] = int(el)

print(sorted(split_text))

three_most_expensive_purchases = 0
for num in sorted(split_text)[-3:]:
    three_most_expensive_purchases += num

# Нужно отсортировать и сложить 3 максимальных
print(three_most_expensive_purchases)

# Здесь пишем код

# assert three_most_expensive_purchases == 202346
