#!/usr/bin/env python3


def filter_longer_than_medium(strings):
    if not strings:
        return []
    lengths = [len(s) for s in strings]
    medium = sum(lengths) / len(lengths)
    print(f"Средняя длина: {medium:.2f}")
    return [s for s in strings if len(s) > medium] #Возвращает строки, длина которых больше средней длины

if __name__ == '__main__':
    raw = input("Введите строки через пробел: ")
    words = raw.split()
    result = filter_longer_than_medium(words)
    if not result:
        print("Нет строк, длина которых больше средней")
    else:
        print(f"Подходящие строки: {result}")
