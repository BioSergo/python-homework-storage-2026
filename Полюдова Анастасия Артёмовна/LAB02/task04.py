#!/usr/bin/env python3


GL: str = 'уеыаоэяиюё'


def check_gl(word: str) -> bool:
    count: int = len([x for x in word.lower() if x in GL])

    return count >= 3


def func4(**kwargs) -> dict:
    result: dict = {}

    for arg_name, arg_value in kwargs.items():
        if isinstance(arg_value, str) and check_gl(arg_value):
            result[arg_name] = arg_value

    return result


if __name__ == '__main__':
    result_1: dict = func4(course='Программирование', mark='три', grade='удовлетворительно')
    print(result_1)
    
