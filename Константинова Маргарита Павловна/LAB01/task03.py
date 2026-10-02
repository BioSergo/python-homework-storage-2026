#!/usr/bin/env python3

import string

GLASNYE: str = "аеёиоуыэюя"
SOGLASNYE: str = "бвгджзйклмнопрстфхцчшщъь"


def analiz_stroki() -> None:
    stroka: str = input("Введите слова через пробел: ")
    slova: tuple[str, ...] = tuple(stroka.split())

    print(f"Кортеж слов: {slova}")
    print(f"Уникальных слов: {len(set(slova))}")

    nizhniy_registr: str = stroka.lower()
    glasnye: int = sum(1 for s in nizhniy_registr if s in GLASNYE)
    soglasnye: int = sum(1 for s in nizhniy_registr if s in SOGLASNYE)
    znaki: int = sum(1 for s in stroka if s in string.punctuation)

    print(f"Гласных: {glasnye}")
    print(f"Согласных: {soglasnye}")
    print(f"Знаков препинания: {znaki}")


if __name__ == "__main__":
    analiz_stroki()
