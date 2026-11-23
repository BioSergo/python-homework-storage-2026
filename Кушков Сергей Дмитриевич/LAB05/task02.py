#!/usr/bin/env python3

import argparse

const = 'div'
OPERATIONS = ('mul', 'sub', 'div', 'add')
MAX_VAR_NUMBER = 1
BASE_ACCURACY = 2

def pseudo_calc(option, val_x, val_y):
    """
    Функция, выполняющая базовые математические операции с числами.

    :param option: Базовая операция
    :param val_x: первое число
    :param val_y: второе число
    :return: результат вычисления
    """
    oper_result = 0

    try:
        if option == 'div':
            oper_result = val_x/val_y
        return oper_result
    except ZeroDivisionError as err:
        print(f'{err}: НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ!!!')

    oper_result = 0
    if option == 'mul':
        oper_result = val_x*val_y
    elif option == 'add':
        oper_result = val_x+val_y
    elif option == 'sub':
        oper_result = val_x-val_y

    return oper_result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Pseudo Calculator",
                                     description="Калькулятор для выполнения базовых вычислений",
                                     epilog="Приятного счёта!")

    parser.add_argument('x', type=float, help='first number')
    parser.add_argument('y', type=float, help='second number')
    parser.add_argument('-op','--operation', default=None, type=str, choices=OPERATIONS,
                        help='Доступные операции выбор' )
    parser.add_argument('-fn','--filename', type=str, nargs=MAX_VAR_NUMBER,
                        help='Имя файла для сохранения результата')
    parser.add_argument('-prs','--precision', type=int, default=BASE_ACCURACY,
                        help='Кол-во знаков после запятой')
    args = parser.parse_args()

    rounded_result = 0
    if args.operation:
        result = pseudo_calc(args.operation, args.x, args.y)
        rounded_result = round(result, args.precision)
        print(rounded_result)
    else:
        print(f'{args.x}, {args.y}')

    if args.filename:
        with open(args.filename, 'a+', encoding="utf-8") as f:
            f.write(f">>Result:{rounded_result}")







