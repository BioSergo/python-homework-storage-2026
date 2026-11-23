#!/usr/bin/env python3

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Утилита для копирования и изменения файла."
    )

    parser.add_argument("--input", required=True, help="Путь к входному файлу")
    parser.add_argument("--output", required=True, help="Путь к выходному файлу")
    parser.add_argument(
        "--replace", help="Замена текста в формате OLD=NEW", default=None
    )
    parser.add_argument(
        "--append-footer", help="Строка для добавления в конец файла", default=None
    )
    parser.add_argument(
        "-f", "--force", action="store_true",
        help="Разрешить перезапись выходного файла",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: входной файл '{args.input}' не найден!")
        exit(2)

    if not args.force:
        try:
            with open(args.output, "r", encoding="utf-8") as f:
                pass
            print(
                f"Ошибка: файл '{args.output}' уже существует. Используйте флаг -f или --force для перезаписи."
            )
            exit(2)
        except FileNotFoundError:
            pass

    replace_count = 0
    if args.replace is not None:
        if "=" not in args.replace:
            print("Ошибка: аргумент --replace должен быть в формате OLD=NEW")
            exit(1)

        parts = args.replace.split("=", 1)
        old_str = parts[0]
        new_str = parts[1]

        replace_count = text.count(old_str)
        text = text.replace(old_str, new_str)

    if args.append_footer is not None:
        if len(text) > 0 and not text.endswith("\n"):
            text = text + "\n"
        text = text + args.append_footer

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Готово! Выполнено замен: {replace_count}")










