#!/usr/bin/env python3


def faktorial_rekursivno(n: int) -> int:
    if n == 0:
        return 1
    return n * faktorial_rekursivno(n - 1)


def faktorial_iterativno(n: int) -> int:
    rezultat: int = 1
    for i in range(2, n + 1):
        rezultat *= i
    return rezultat


def vychislenie_faktoriala() -> None:
    while True:
        vvod: str = input("Введите целое число: ")
        if vvod.isdigit():
            break
        print("Нужно ввести целое число.")

    n: int = int(vvod)
    print(f"Рекурсивно: {faktorial_rekursivno(n)}")
    print(f"Итеративно: {faktorial_iterativno(n)}")


if __name__ == "__main__":
    vychislenie_faktoriala()
