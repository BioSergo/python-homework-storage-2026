#!/usr/bin/env python3


def sortirovat(chisla: list[float], po_ubyvaniyu: bool) -> list[float]:
    return sorted(chisla, reverse=po_ubyvaniyu)


if __name__ == "__main__":
    while True:
        vvod: str = input("Введите числа через пробел: ")
        try:
            chisla: list[float] = [float(x) for x in vvod.split()]
        except ValueError:
            print("Нужно ввести числа через пробел.")
            continue
        if chisla:
            break
        print("Введите хотя бы одно число.")

    while True:
        poryadok: str = input("1 - по возрастанию, 2 - по убыванию: ")
        if poryadok in {"1", "2"}:
            break
        print("Введите только 1 или 2.")

    rezultat = sortirovat(chisla, poryadok == "2")
    print(rezultat)
