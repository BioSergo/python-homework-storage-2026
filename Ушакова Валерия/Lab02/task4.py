#!/usr/bin/env python3


VALUES : tuple= ('у','е','ы','а','о','э','я','и','ю','e','y','u','i','o','a')

def count_vowels(text):
    count = 0
    for c in text.lower():
        if c in VALUES:
            count += 1
    return count

def filtr(**kwargs):

    for key, value in kwargs.items():
        if not isinstance(value, str):
            print(f'{key} — не строка\n')
            continue

        if count_vowels(value) >= 3:
            result[key] = value

    return result

if __name__ == '__main__':
    data = {}
    result = {}
    print('Введите пары: сначала ключ, потом значение.')
    print('Для завершения введите нажмите Enter')

    while True:
        key = input('Ключ: ').strip()

        if not key:
            break

        value = input('Значение: ').strip()
        data[key] = value

    result = filtr(**data)
    print(f'\nПодходящие: {result}')
