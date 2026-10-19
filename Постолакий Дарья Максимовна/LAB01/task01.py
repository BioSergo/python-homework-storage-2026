#!/usr/bin/env python3
def different_numbers(user_data):
    nums = []
    for i in user_data:
        try:
            val = float(i)
            nums.append(val)
        except ValueError:
            continue
    return nums

if __name__ == '__main__':
    user_input = input("Введите что-то через пробел (желательно числа):\n")
    user_data = user_input.split()
    nums = different_numbers(user_data)
    if not nums:
        print("Чисел нет")
    elif len(nums) == len(set(nums)):
        print("Все числа различны")
    else:
        duplicates = [num for num in set(nums) if nums.count(num) > 1]
        duplicates.sort()
        print(f"Есть повторяющиеся числа:", *duplicates)
