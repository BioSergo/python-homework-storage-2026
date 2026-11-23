#!/usr/bin/env python3

import argparse
import random


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIALS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
MIN_PASSWORD_LENGHT = 8
MAX_PASSWORD_LENGHT = 64
MIN_PASSWORD_VALUE = 1


if __name__ == "__main__"


    parser = argparse.ArgumentParser(description="Генератор случайных паролей.")

    parser.add_argument("-l", "--length", type=int, default=12,
        help="Длина пароля (от 8 до 64, по умолчанию 12)",
    )
    parser.add_argument("-c", "--count", type=int, default=1,
        help="Количество паролей (по умолчанию 1)",
    )
    parser.add_argument("--no-digits", action="store_true", help="Исключить цифры из пароля"
    )
    parser.add_argument("--no-special", action="store_true",
        help="Исключить специальные символы из пароля",
    )
    parser.add_argument("-o", "--output", default=None, help="Путь к файлу для сохранения паролей"
    )

    args = parser.parse_args()

    if args.length < MIN_PASSWORD_LENGHT or args.length > MAX_PASSWORD_LENGHT:
        print("Ошибка: длина пароля должна быть в диапазоне от 8 до 64 символов!")
        exit(2)

    if args.count < MIN_PASSWORD_VALUE:
        print("Ошибка: количество паролей должно быть больше 0!")
        exit(2)

    alphabet = LETTERS

    if not args.no_digits:
        alphabet = alphabet + DIGITS

    if not args.no_special:
        alphabet = alphabet + SPECIALS

    if len(alphabet) == 0:
        print("Ошибка: не осталось ни одного символа для генерации пароля!")
        exit(2)

    passwords = []
    for i in range(args.count):
        password = ""
        for j in range(args.length):
            random_char = random.choice(alphabet)
            password = password + random_char
        passwords.append(password)

    for p in passwords:
        print(p)

    if args.output is not None:
        with open(args.output, "w", encoding="utf-8") as f:
            for p in passwords:
                f.write(p + "\n")
        print(f"Пароли успешно сохранены в файл '{args.output}'.")





