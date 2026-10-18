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

def check_positive_int(prompt):
    while True:
        raw = input(prompt)
        if raw.isdigit():
            return int(raw)
        print("Должно быть целое неотрицательное число, попробуйте снова")

if __name__ == '__main__':
    n = check_positive_int("Введите целое неотрицательное число: ")
    print(f"Факториал(рекурсивно): {factorial_recursive(n)}")
    print(f"Факториал(итеративно): {factorial_iterative(n)}")
