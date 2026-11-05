#usr/bin/venv python3

from functools import reduce

STANDARD_DELIMITED = " "

def main():
    """
    Запрашивает строки у пользователя
    :return: список строк
    """

    user_input = input("Строки через пробел:\n").split(STANDARD_DELIMITED)

    return user_input


if __name__ == '__main__':
    words = main()

    filter_1 = list(filter(lambda x: len(x) >= 7, words))
    print(f"Первый шаг: \n{filter_1}\n")

    analyzing = list(map(lambda x: (x, len(x)), filter_1))
    print(f"Второй шаг: \n{analyzing}\n")

    max_len_word = reduce(lambda a,b: a if a[1] > b[1] else b, analyzing)
    print(f"Третий шаг: \n{max_len_word}\n")

    all_words_len = reduce(lambda a,b: a + b[1], analyzing, 0)
    print(f"Четвёртый шаг: \n{all_words_len}\n")


