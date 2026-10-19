#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '


def insertion_sort(spisok: list[int], descending_order: bool):
    n: int = len(spisok)

    for i in range(1, n):
        j: int = i

        if descending_order:
            while j > 0 and spisok[j] > spisok[j - 1]:
                spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
                j -= 1
        else:
            while j > 0 and spisok[j] < spisok[j - 1]:
                spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
                j -= 1

    return spisok


if __name__ == '__main__':
    text: str = input('Введите числа: ').strip()

    if not text:
        print('Пустовато..')
    else:
        try:
            result_1: list[int] = [int(x) for x in text.split(STANDARD_DELIMITED)]
        except ValueError:
            print('Введите только целые числа')
        else:
            choice: str = input('Выберите: 1 - по возрастанию, 2 - по убыванию: ').strip()

            if choice == '1':
                result_2: list[int] = insertion_sort(result_1, False)
                print('По возрастанию:', result_2)

            elif choice == '2':
                result_2: list[int] = insertion_sort(result_1, True)
                print('По убыванию:', result_2)

            else:
                print('???')
                
