file_path = input("Введите путь до файла: ")

file_path_split = file_path.split("\\")

disc_name = file_path_split[0][0]
folder = file_path_split[1]
file_name = file_path_split[-1].split(".")[0]

print("Название файла: " + str(file_name))
print("Название диска: " + str(disc_name))
print("Название корневой папки: " + str(folder))
