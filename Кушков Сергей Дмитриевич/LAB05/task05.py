#!/usr/bin/env python3

import argparse
import random


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIALS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
MIN_PASSWORD_VALUE = 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Парольчики",
                                     description="Генератор случайных паролей.")

    parser.add_argument("-l", "--length", type=int, default=12,
        help="Длина пароля",
    )
    parser.add_argument("-c", "--count", type=int, default=1,
        help="Количество паролей",
    )
    parser.add_argument("--no-digits", action="store_true",
                        help="Исключить цифры из пароля"
    )
    parser.add_argument("--no-special", action="store_true",
        help="Исключить специальные символы из пароля",
    )
    parser.add_argument("-o", "--output", default=None,
                        help="Путь к файлу для сохранения паролей"
    )

    args = parser.parse_args()

    if args.length < MIN_PASSWORD_LENGTH or args.length > MAX_PASSWORD_LENGTH:
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
        print(f"Пароли сохранены в файл '{args.output}'")





