#!/usr/bin/env python3


def only_numbers(text):
    numbers = []
    for token in text.split():
        try:
            numbers.append(float(token))
        except ValueError:
            pass
    return numbers

def sort_max(numbers): # По возрастанию
    return sorted(numbers)

def sort_min(numbers): # По убыванию
    return sorted(numbers, reverse=True)

def read_mode():
    print("Выберите режим сортировки:\n1 — по возрастанию\n2 — по убыванию")
    while True:
        result = input("Ваш выбор: ")
        if result in ('1', '2'):
            return result
        print("Неверный выбор режима, попробуйте снова")

if __name__ == '__main__':
    mode = read_mode()
    raw = input("Введите числа через пробел: ")
    nums = only_numbers(raw)
    if not nums:
        print("Чисел нет")
    elif mode == '1':
        print(*sort_max(nums))
    else:
        print(*sort_min(nums))
