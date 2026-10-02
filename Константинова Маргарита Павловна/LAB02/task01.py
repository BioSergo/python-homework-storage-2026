#!/usr/bin/env python3


def dlinnee_srednego(stroki: list[str]) -> list[str]:
    if not stroki:
        return []
    srednyaya_dlina: float = sum(len(s) for s in stroki) / len(stroki)
    return [s for s in stroki if len(s) > srednyaya_dlina]


def filtratsiya_strok() -> None:
    stroki: list[str] = input("Введите строки через пробел: ").split()
    print(dlinnee_srednego(stroki))


if __name__ == "__main__":
    filtratsiya_strok()
