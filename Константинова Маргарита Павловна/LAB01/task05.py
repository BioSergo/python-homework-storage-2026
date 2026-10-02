#!/usr/bin/env python3

import math


def tretya_storona() -> None:
    vybor: str = input("1 - два катета, 2 - гипотенуза и катет: ")

    if vybor == "1":
        a: float = float(input("Первый катет: "))
        b: float = float(input("Второй катет: "))
        storona: float = math.sqrt(a ** 2 + b ** 2)
    else:
        a = float(input("Гипотенуза: "))
        b = float(input("Известный катет: "))
        storona = math.sqrt(a ** 2 - b ** 2)

    print(f"Третья сторона: {storona:.2f}")


if __name__ == "__main__":
    tretya_storona()
