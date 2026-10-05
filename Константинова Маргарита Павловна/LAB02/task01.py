#!/usr/bin/env python3


def dlinnee_srednego(stroki: list[str]) -> list[str]:
    if not stroki:
        return []
    srednyaya_dlina: float = sum(len(s) for s in stroki) / len(stroki)
    return [s for s in stroki if len(s) > srednyaya_dlina]


if __name__ == "__main__":
    stroki: list[str] = input("Введите строки через пробел: ").split()
    rezultat = dlinnee_srednego(stroki)
    print(rezultat)
