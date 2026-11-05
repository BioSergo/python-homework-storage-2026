#!/usr/bin/env python3

STANDARD_DELIMITED = " "

if __name__ == '__main__':

    user_input = input(f"Введите целые числа через пробел:\n").split(STANDARD_DELIMITED)

    num_list =[]

    for i in user_input:
        try:
            num = int(i)
            num_list.append(num)
        except ValueError:
            print(f'{i} is not a number')
            continue

    for y in num_list:
        mood_check = lambda x: (
                                "positive even" if x > 0 and x % 2 == 0 else
                                "positive odd" if x > 0 else
                                "negative" if x < 0 else "zero"
                                )

        print(f"{y} is {mood_check(y)}")


