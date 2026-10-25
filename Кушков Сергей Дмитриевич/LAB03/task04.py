#usr/bin/venv python3

from functools import reduce

def main():
    """
    Функция, которая принимает от пользователя строки и выполняет:
        +Оставляет только слова длиной не менее 7 символов.
        +Оставшиеся слова объединяет в пару с их длиной.
        +Находит слово с максимальной длиной.
        +Считает суммау букв всех отфильтрованных слов.

    """

    user_input = input("Строки через пробел:\n").split()

    filter_1 = list(filter(lambda x: len(x) >= 7, user_input))
    print(f"Первый шаг: \n{filter_1}\n")

    analyzing = list(map(lambda x: (x, len(x)), filter_1))
    print(f"Второй шаг: \n{analyzing}\n")

    max_len_word = reduce(lambda a,b: a if a[1] > b[1] else b, analyzing)
    print(f"Третий шаг: \n{max_len_word}\n")

    all_words_len = reduce(lambda a,b: a + b[1], analyzing, 0)
    print(f"Четвёртый шаг: \n{all_words_len}\n")

if __name__ == '__main__':
    main()



