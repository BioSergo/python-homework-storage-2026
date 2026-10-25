#usr/bin/venv python3


def repeat_decor(n):
    """
    Функция, которая вызывает декоратор n-раз.

    :param n: Количество повторений
    :type n: int
    :return: Декоратор ultimate_decorator
    :rtype: function
    """
    def ultimate_decorator(func):
        def some_wrapper():
            something = []
            for i in range(1, n+1):
                print(f"Printed 'Hello World' {i} times")
                thing = func()
                something.append(thing)
            return something

        return some_wrapper
    return ultimate_decorator

@repeat_decor(n=5)
def helloworld():
    """
    Функция, которая возвращает строку с приветствием.
    :return:
    """
    return "Hello World!!!"

if __name__ == "__main__":
    all_result_list = helloworld()
    print(all_result_list)

