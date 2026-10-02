#!/usr/bin/env python3

ALFAVIT: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def primenit_shifr() -> None:
    vybor: str = input("1 - текст в числа, 2 - числа в текст: ")

    if vybor == "1":
        tekst: str = input("Введите текст: ").lower()
        chisla: list[int] = [ALFAVIT.index(s) + 1 if s in ALFAVIT else 0 for s in tekst]
        print(*chisla)
    else:
        chisla = [int(x) for x in input("Введите числа через пробел: ").split()]
        tekst = "".join(ALFAVIT[n - 1] if n > 0 else " " for n in chisla)
        print(tekst)


if __name__ == "__main__":
    primenit_shifr()
