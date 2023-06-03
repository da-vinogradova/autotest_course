# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from pathlib import Path

# Создаем относительный путь до файла с заданием. Из-за того, что не знаем слэши, разбиваем папки через запятую
path = Path('test_file', 'task1_data.txt')
# Относительный путь до файла с ответом
path_new = Path('test_file', 'task1_answer.txt')

# Создаем абсолютный путь, чтобы работало все и везде. Сджойним путь до текущей рабочей
# директории с относительным путем файла
abs_path = Path.cwd().joinpath(path)

# откроем файл с данными
task1_file = open(abs_path)

# Создадим новый файл, чтобы в него сразу писать инфу
new_file = open(Path.cwd().joinpath(path_new), "w+")

try:
    # Записываем содержимое исходного файла в строку
    task1_text = task1_file.read()

    # Список с цифрами
    list_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Удаляем цифры из строки
    for let in task1_text:
        if let not in list_num:
            new_file.write(let)

# Закрываем все файлы
finally:
    new_file.close()
    task1_file.close()


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
