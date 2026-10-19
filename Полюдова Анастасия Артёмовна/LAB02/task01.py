#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '


def func1(value: list[str]):
    var_1: list[int] = [len(x) for x in value]
    var_2: float = sum(var_1) / len(var_1)
    f_result: list[str] = [x for x in value if len(x) > var_2]

    return f_result


if __name__ == '__main__':
    text: str = input('Введите слова: ').strip()

    if not text:
        print('Пустовато..')
    else:
        result_1: list[str] = text.split(STANDARD_DELIMITED)
        result_2: list[str] = func1(result_1)

        if not result_2:
            print('Нет строк длиннее среднего значения')
        else:
            print(result_2)
            
