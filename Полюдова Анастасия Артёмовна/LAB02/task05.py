#!/usr/bin/env python3


def fact_rec(n: int):
    if n <= 1:
        return 1

    return n * fact_rec(n - 1)


def fact_iter(n: int):
    result: int = 1

    for i in range(2, n + 1):
        result *= i

    return result


def func5():
    text: str = input('Введите целое число: ').strip()

    if not text:
        print('Пустовато..')
        return None

    try:
        number: int = int(text)
    except ValueError:
        print('Нужно ввести целое число')
        return None

    if number < 0:
        print('Не нужно вводить отрицательное число')
        return None

    return number


if __name__ == '__main__':
    result_1 = func5()

    if result_1 is not None:
        var_1: int = fact_rec(result_1)
        var_2: int = fact_iter(result_1)
        print('Рекурсивный метод:', var_1)
        print('Итеративный метод:', var_2)
        
