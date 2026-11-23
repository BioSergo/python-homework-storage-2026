#!/usr/bin/env python3

import argparse

MAX_AGE_VALUE = 120
MIN_AGE_VALUE = 0

if __name__ == '__main__':
    ...
    #age_var=your_age(121)
    parser = argparse.ArgumentParser(
        prog='Greetings',
        description='Greets beloved users <3!',
        epilog='love yourself!',
    )

    parser.add_argument("greet_name", help="Имя пользователя",
                        type=str, nargs="?",default="User")
    parser.add_argument('-a','--age', help='Ваш возраст', type=int)
    parser.add_argument('-g','--greet_you', help='Флаг приветствия', action='store_true')
    args = parser.parse_args()

    if args.age is not None:
        if MAX_AGE_VALUE < args.age or MIN_AGE_VALUE >  args.age:
            parser.error(
                message=f"Возраст вне диапазона! Должен быть между {MIN_AGE_VALUE} и {MAX_AGE_VALUE}"
            )

    if args.greet_you and args.age is not None:
        print(f'Уважаемый(-ая), {args.greet_name} вам {args.age}')
    elif args.greet_you:
        print(f'Уважаемый(-ая) {args.greet_name}')
    elif args.age is not None:
        print(f"{args.greet_name} вам {args.age}")
    else:
        print(f'{args.greet_name}')





