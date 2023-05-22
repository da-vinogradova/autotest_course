### ЦИКЛЫ ###
# range() позволяет получить только элементы списка. stop - ограничение генерации
for i in range(stop=4):
     print(i)

# step - шаг, с которым генерировать числа
for i in range(start=2, stop=10, step=3):
         print(i)

# Если же нам кроме самих элементов потребуются их индексы, можно воспользоваться функцией range(),
# передав в нее длину списка len(my_list)
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
     print(i)  # 0 1 2 3 4

# enumerate() – позволяет получить сразу индекс элемента и его значение.
spisok = [16, 46, 26, 36]
for i in enumerate(spisok):
     print(i)
(0, 16)
(1, 46)
(2, 26)
(3, 36)

### Вложенные циклы ###

strange_phonebook = [
     ["Alex", "Andrew", "Aya", "Azazel"],
     ["Barry", "Bill", "Brave", "Byanka"],
     ["Casey", "Chad", "Claire", "Cuddy"],
     ["Dana", "Ditrich", "Dmitry", "Donovan"] ]
# это список списков, где каждый подсписок состоит из строк
# следовательно можно (зачем-то) применить тройной for
# для посимвольного чтения всех имён
# и вывода их в одну строку
for letter in strange_phonebook:
     for name in letter:
         for character in name:
             print(character, end=' ')
# >>> A l e x A n d r e w A y a A z a z e l B a r ...  end в принте позволяет вывести все в одну строку, а не с новой

### Генераторы списков ###
# список квадратов чисел
squares = [x**2 for x in range(1, 11)]

# список квадратов чисел с условием
even_squares = [x**2 for x in range(1, 11) if x%2 == 0]

# Примеры
word = 'Hello'
numbers = [1, 14, 5, 9, 12]
words = ['one', 'two', 'three', 'four', 'five', 'six']

[0 for i in range(10)]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[i ** 2 for i in range(1, 8)]
#[1, 4, 9, 16, 25, 36, 49]

[i * 10 for i in numbers]
#[10, 140, 50, 90, 120]

[c * 2 for c in word]
#['HH', 'ee', 'll', 'll', 'oo']

[m[0] for m in words]
#['o', 't', 't', 'f', 'f', 's']

[i for i in numbers if i < 10]
#[1, 5, 9]

[m[0] for m in words if len(m) == 3]
#['o', 't', 's']


### BOOLEAN ###
# Логика простая - если размер списка или строки равен нулю, то переменная bool в Python будет равна False.
# 0 - это так же False. Все остальные значения, отличные от 0 или с длиной больше 0 будут True.


###  УСЛОВИЯ  ###
if a < b:
     rez = a + b
else:
     rez = a - b

# общий вид if/else в одну строку
x = a if condition else b


### Break, continue и pass ###
# break позволяет досрочно прервать цикл
# continue начинает следующий проход цикла, минуя оставшееся тело цикла.
# Простыми словами continue позволяет пропустить часть цикла при возникновении препятствия и вернуться к началу цикла.
# Оператор pass означает, что ничего делать не нужно

### None ###
# Обычно None используется, когда вы хотите создать переменную, но пока не задаете значение
languages = ["C", "C++", "Python", "Java", "Go"]
position = None
for i, element in enumerate(languages):
     if element == "Python":
         position = i
         break
if position is None:
     print("Элемент не найден.")
else:
     print("Элемент находится на позиции:", position)