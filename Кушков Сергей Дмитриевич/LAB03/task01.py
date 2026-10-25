#!/usr/bin/env python3


if __name__ == '__main__':

    user_input = input(f"Введите целые числа:\n").split()

    num_list =[]
    try:
        num_list = [int(i) for i in user_input]
    except ValueError:
        print("Введите только целые числа")

    for y in num_list:
        mood_check = lambda x: (
                                "positive even" if x > 0 and x % 2 == 0 else
                                "positive odd" if x > 0 else
                                "negative" if x < 0 else "zero"
                                )

        print(f"{y} is {mood_check(y)}")


