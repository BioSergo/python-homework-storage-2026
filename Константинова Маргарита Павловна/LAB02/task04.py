#!/usr/bin/env python3

GLASNYE: str = "аеёиоуыэюя"
MINIMUM_GLASNYKH: int = 3


def stroki_s_tremya_glasnymi(**argumenty: object) -> dict[str, object]:
    rezultat: dict[str, object] = {}

    for klyuch, znachenie in argumenty.items():
        if isinstance(znachenie, str):
            kolichestvo: int = sum(1 for s in znachenie.lower() if s in GLASNYE)
            if kolichestvo >= MINIMUM_GLASNYKH:
                rezultat[klyuch] = znachenie

    return rezultat


if __name__ == "__main__":
    print(stroki_s_tremya_glasnymi(imya="бабушка", chislo=5, gorod="аллея"))
