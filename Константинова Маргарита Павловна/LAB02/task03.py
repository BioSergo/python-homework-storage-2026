#!/usr/bin/env python3


def proizvedenie_tselykh(*argumenty: object) -> int | None:
    tselye: list[int] = [argument for argument in argumenty if type(argument) is int]

    if not tselye:
        for argument in argumenty:
            print(argument, type(argument))
        return None

    proizvedenie: int = 1
    for argument in tselye:
        proizvedenie *= argument
    return proizvedenie


if __name__ == "__main__":
    print(proizvedenie_tselykh(2, "slovo", 3.5, 4))
    print(proizvedenie_tselykh("a", 1.5, [1, 2]))
