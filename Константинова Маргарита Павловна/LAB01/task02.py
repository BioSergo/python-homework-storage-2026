#!/usr/bin/env python3

KURSY: tuple[str, ...] = (
    "Структуры данных",
    "Высшая математика",
    "Физика",
    "История России",
    "Органическая химия",
)

OTSENKA_OT: int = 3
OTSENKA_DO: int = 5


def schitat_otsenku(kurs: str) -> int:
    while True:
        otsenka = input(f"Оценка по курсу {kurs}: ")
        if otsenka.isdigit() and OTSENKA_OT <= int(otsenka) <= OTSENKA_DO:
            return int(otsenka)
        print(f"Оценка должна быть целым числом от {OTSENKA_OT} до {OTSENKA_DO}.")


def statistika_po_kursam() -> None:
    otsenki_po_kursam: dict[str, list[int]] = {kurs: [] for kurs in KURSY}

    while True:
        imya = input("Имя студента (Enter для завершения): ")
        if not imya:
            break
        for kurs in KURSY:
            otsenki_po_kursam[kurs].append(schitat_otsenku(kurs))

    if not otsenki_po_kursam[KURSY[0]]:
        print("Студенты не введены.")
        return

    for kurs, otsenki in otsenki_po_kursam.items():
        sredniy = sum(otsenki) / len(otsenki)
        print(
            f"{kurs}: средний балл {sredniy:.2f}, "
            f"минимальная {min(otsenki)}, максимальная {max(otsenki)}"
        )


if __name__ == "__main__":
    statistika_po_kursam()
