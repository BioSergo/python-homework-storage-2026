#!/usr/bin/env python3


def sortirovat(chisla: list[float], po_ubyvaniyu: bool) -> list[float]:
    return sorted(chisla, reverse=po_ubyvaniyu)


def sortirovka_chisel() -> None:
    vvod: str = input("Введите числа через пробел: ")
    chisla: list[float] = [float(x) for x in vvod.split()]
    poryadok: str = input("1 - по возрастанию, 2 - по убыванию: ")
    print(sortirovat(chisla, poryadok == "2"))


if __name__ == "__main__":
    sortirovka_chisel()
