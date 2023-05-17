first_string = input('Введите первую строку: ')
second_string = input('Введите вторую строку: ')

# Найдем индексы символов из первой строки во второй строке
first_sym_index = second_string.find(first_string[0])
second_sym_index = second_string.find(first_string[1])
third_sym_index = second_string.find(first_string[2])

# Находим минимальный отрезок
min_ind = min(first_sym_index, second_sym_index, third_sym_index)
max_ind = max(first_sym_index, second_sym_index, third_sym_index)

# Выводим данные
print(second_string[min_ind:max_ind+1])
