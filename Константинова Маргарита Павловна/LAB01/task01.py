#!/usr/bin/env python3


def vse_razlichny(chisla: list[float]) -> bool:
    return len(chisla) == len(set(chisla))


def proverka_chisel() -> None:
    vvod: str = input("Введите числа через пробел: ")
    chisla: list[float] = [float(x) for x in vvod.split()]

    if vse_razlichny(chisla):
        print("Все числа различны.")
    else:
        print("Среди чисел есть повторяющиеся значения.")


if __name__ == "__main__":
    proverka_chisel()
