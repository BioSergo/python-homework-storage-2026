#!/usr/bin/env python3

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Фильтр для строк")
    parser.add_argument('string',nargs='*', type=str,
                        help="Одна или несколько строк" )
    parser.add_argument('-cs','--count', action='store_true',
                        help="Флаг подсчета строк")
    parser.add_argument('-u','--unique', action='store_true',
                        help='Вывести только уникальные строки')
    parser.add_argument('-m','--min-len', type=int, default=0,
                        help='Длина строк не меньше указаного значения')
    parser.add_argument('--sort', type=str, default='none',
                        help='Тип сортировки')
    args = parser.parse_args()

    if args.string is None:
        parser.error(
            message="Ошибка не передали ни одной строки для обработки"
        )

    if args.sort not in ["asc", "desc", None]:
        parser.error(
            message=f"Неверное значение для --sort: "
                    f"'{args.sort}'. Используйте asc, desc или none."
        )

    result = args.string

    filtered = []
    for s in result:
        if len(s) >= args.min_len:
            filtered.append(s)
    result = filtered

    if args.unique:
        unique_list = []
        for s in result:
            if s not in unique_list:
                unique_list.append(s)
        result = unique_list

    if args.sort == 'asc':
        result.sort()
    elif args.sort == 'desc':
        result.sort(reverse=True)

    if args.count:
        print(len(result))
    else:
        for s in result:
            print(s)






