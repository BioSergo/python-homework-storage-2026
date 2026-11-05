#usr/bin/venv python3

import random

def main():
    """
    Функция, которая создаёт список из 20 случайных целых чисел и
    фильтрует их по 3 критерия.

    :return: Список словарей
    """

    random_numbers_list = [random.randint(-100, 100) for _ in range(20)]

    list_of_results = []

    filters = [
        lambda x: x % 3 == 0 and x % 9 != 0,
        lambda x: abs(x) > 20,
        lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20
    ]

    for condition in filters:
        filtered_list = list(filter(condition, random_numbers_list))
        length = len(filtered_list)
        dict_param = {"numbers": filtered_list, "length": length}
        list_of_results.append(dict_param)

    return list_of_results


if __name__ == "__main__":
    result = main()

    for z in result:
        print(f'{z["numbers"]}\nlength: {z["length"]}\n')


