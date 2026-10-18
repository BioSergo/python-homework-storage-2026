#!/usr/bin/env python3


STANDARD_DELIMITED = ','

def hay(*args):
    integers = [a for a in args if isinstance(a, int)]

    if not integers:
        print('Целых нет, аргументы:')
        for a in args:
            print(f'{a} — {type(a).__name__}')
        return

    res = 1
    for n in integers:
        res *= n
    return res


if __name__ == '__main__':
    text = input(f'Введите значения через "{STANDARD_DELIMITED}":\n')
    parts = text.replace(STANDARD_DELIMITED, ' ').split()

    values = []
    for p in parts:
        if p.isdigit():
            values.append(int(p))
        elif p.replace('.', '', 1).replace('-', '', 1).isdigit():
            values.append(float(p))
        else:
            values.append(p)

    print('Введенные значения:')
    for v in values:
        print(f'{v} - {type(v).__name__}')

    print('Произведение:', hay(*values))
