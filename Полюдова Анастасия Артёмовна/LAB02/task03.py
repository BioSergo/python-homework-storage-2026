#!/usr/bin/env python3


def func3(*args):
    result: int = 1
    check_int: bool = False

    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            result *= arg
            check_int = True

    if check_int:
        return result

    for arg in args:
        print(arg, '-', type(arg))

    return None


if __name__ == '__main__':
    result_1 = func3(3.22, True, 'аргумент')
    result_2 = func3(1, 2, 3)
    print('Произведение аргументов:', result_2)
    
