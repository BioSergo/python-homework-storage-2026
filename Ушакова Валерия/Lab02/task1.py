#!/usr/bin/env python3


STANDARD_DELIMITED: str= ','
def longer(words: list) -> list:
    if not words:
        return []

    lengths = [len(word) for word in words]
    average = sum(lengths) / len(lengths)

    return [word for word in words if len(word) > average]

if __name__ == '__main__':
    print(f'Введите слова,используя "{STANDARD_DELIMITED}" как делимитр:\n')

    words = []
    while not words:
        text = input().strip()

        words= text.replace(',', ' ').split()

        if not words:
            print('Пусто пусто')

    result = longer(words)
    average = sum(len(w) for w in words) / len(words)

    print(f'Слова: {words}')
    print(f'Средняя длина: {average:}')
    print(f'Слова длиннее среднего: {result}')
 
