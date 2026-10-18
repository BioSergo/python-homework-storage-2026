#!/usr/bin/env python3
import math

def only_positive_number(prompt):
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print("Это не число, попробуйте снова")
            continue
        if value > 0:
            return value
        print("Число должно быть положительным")

def find_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def find_leg(a, c):
    if c < a:
        c, a = a, c
    return math.sqrt(c**2 - a**2)

if __name__ == '__main__':
    print("Что известно?\n1 — два катета (ищем гипотенузу)\n2 — катет и гипотенуза (ищем второй катет)")
    mode = input("Ваш выбор: ")
    if mode == '1':
        a = only_positive_number("Первая сторона: ")
        b = only_positive_number("Вторая сторона: ")
        c = find_hypotenuse(a, b)
        print(f"Гипотенуза: {c:.2f}")
    elif mode == '2':
        a = only_positive_number("Первая сторона: ")
        c = only_positive_number("Вторая сторона: ")
        b = find_leg(c, a)
        print(f"Второй катет: {b:.2f}")
    else:
        print("Неверный выбор режима")
