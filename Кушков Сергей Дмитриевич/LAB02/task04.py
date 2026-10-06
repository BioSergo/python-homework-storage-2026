#!/usr/bin/env python3

target_letters = set("уыоэеаяиюёУЫОЭЕАЯИЮЁ")

def letter_dict(**words):

    filtered_dict = {}
    for key, value in words.items():

        if isinstance(value, str):

            char_num = 0
            for char in value:
                if char in target_letters:
                    char_num += 1

            if char_num >= 3:
                filtered_dict[key] = value

    return filtered_dict


if __name__ == '__main__':

    print(letter_dict(
                author = "Тоби",
                type = "Сказка",
                name = "Подземелье",
                main_hero = "Фриск",
                num = 1,
                route = "Пацифизм"
                ))


