#!/usr/bin/env python3


def proizvedenie_tselykh(*args: object) -> int | None:
    tselye: list[int] = [arg for arg in args if type(arg) is int]

    if not tselye:
        return None

    proizvedenie: int = 1
    for arg in tselye:
        proizvedenie *= arg
    return proizvedenie


if __name__ == "__main__":
    rezultat_1 = proizvedenie_tselykh(2, "slovo", 3.5, 4)
    rezultat_2 = proizvedenie_tselykh("a", 1.5, [1, 2])
    print(rezultat_1)
    print(rezultat_2)
