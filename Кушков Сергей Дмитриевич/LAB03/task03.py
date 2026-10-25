#usr/bin/venv python3

import random

def main():
    """
    Функция, которая создаёт список из 20 случайных чисел и
    фильтрует их по критериям:
        +числа, которые делятся на 3, но не делятся на 9;
        +числа, абсолютное значение которых больше 20;
        +числа, которые одновременно удовлетворяют обоим условиям.

    :return: Список списков, где внутри лежит список целых чисел и целое число
    :rtype: list[list[list[int], int]]
    """

    random_numbers_list = [random.randint(-100, 100) for _ in range(20)]
    results = []

    filters = [
        lambda x: x % 3 == 0 and x % 9 != 0,
        lambda x: abs(x) > 20,
        lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20
        ]

    for condition in filters:
        filtered_list = list(filter(condition, random_numbers_list))
        length = len(filtered_list)
        results.append([filtered_list, length])

    return results

if __name__ == "__main__":
    hello = main()
    for z,y in hello:
        print(f'{z}\nlength: {y}\n')