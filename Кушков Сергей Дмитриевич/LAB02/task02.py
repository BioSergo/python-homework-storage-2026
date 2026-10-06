#!/usr/bin/env python3

STANDARD_DELIMITED = " "
SEMICOLON = "; "

def header():

    while True:
        try:
            numbers_list = []
            user_input = input(f"Введите числа через пробел:\n").split()

            for value in user_input:
                value = value.replace(',','.')
                if value.isdigit():
                    numbers_list.append(int(value))
                else:
                    numbers_list.append(float(value))

            user_input = input(f"Выберите способ сортировки:\n\n{STANDARD_DELIMITED}0. по возрасстанию\n{STANDARD_DELIMITED}1. по убыванию"
                                f"\n\nВведите индекс:\n")
            if user_input in ('1','0'):
                if user_input == '0':
                    sorted_numbers = SEMICOLON.join(str(x) for x in sorted(numbers_list))
                    print(f'Результат  сортировки по возрастанию: \n{sorted_numbers}')
                    return sorted_numbers, user_input
                else:
                    sorted_numbers = SEMICOLON.join(str(x) for x in sorted(numbers_list, reverse=True))
                    print(f'Результат сортировки по убыванию \n{sorted_numbers}')
                    return sorted_numbers, user_input
            else:
                print('Индекс вне диапазона')

        except ValueError:
                    print(f"Ошибка! введите только числа!")

if __name__ == '__main__':
    result, preference = header()
    if preference == "0":
        print(f'Результат  сортировки по возрастанию:{STANDARD_DELIMITED}\n{result}')
    else:
        print(f'Результат сортировки по убыванию:{STANDARD_DELIMITED}\n{result}')




