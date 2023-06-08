# При вызове этой функции она уже считается декорированной
@dec
def my_func(arg):
    print(f"Тестовая функция {arg}")
    return arg


def dec(func):
    def wrapper(*args, **kwargs):
        print(1)
        res = func(*args, **kwargs)
        print(2)
        return res
    return wrapper

# f = decorat(my_func) Эту запись мы заменили @decorat
# f("Вот сюда пишем текст")
