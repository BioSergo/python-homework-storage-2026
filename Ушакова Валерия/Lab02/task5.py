#!/usr/bin/env python3

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
        text = input('Введите целое неотрицательное число:\n').strip()

        try:
            n = int(text)
        except ValueError:
            print('Это не число!\n')
        else:
            if n < 0:
                print('Число должно быть неотрицательным\n')
            else:
                print(f'Рекурсивно: {factorial_recursive(n)}')
                print(f'Итеративно: {factorial_iterative(n)}')
