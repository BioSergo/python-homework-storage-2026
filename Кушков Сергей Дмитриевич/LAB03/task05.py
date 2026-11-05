#usr/bin/venv python3

DEFAULT_REPEAT_COUNTER = 5

def repeat_decor(n):
    """
    Функция, которая вызывает декоратор n-раз.

    :param n: Количество повторений
    :return: Декоратор ultimate_decorator
    """

    def ultimate_decorator(func):
        def some_wrapper(*args, **kwargs):
            something = []
            for i in range(1, n+1):
                print(f"Printed 'Hello World' {i} times by '{func.__name__}'")
                thing = func(*args, **kwargs)
                something.append(thing)
            return something
        return some_wrapper

    return ultimate_decorator

@repeat_decor(DEFAULT_REPEAT_COUNTER)
def helloworld(name):
    """
    Функция, которая получает имя пользователя и возвращает строку с приветствием.
    :return: Строка с приветствием
    """
    return f"Hello, World and {name}"

if __name__ == "__main__":
    all_result_list = helloworld("Sergey")
    print(all_result_list)




