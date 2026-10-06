#!/usr/bin/env python3


def string_length(string_list):

    if not string_list:
        return "Список пуст"

    true_strings = []
    total_length = 0
    valid_string_list = []

    for string in string_list:
        if not isinstance(string, str):
            print(f"Был пропущен эл-нт {string}, так как не является строчкой")
        else:
            total_length += len(string)
            valid_string_list.append(string)
    average_length = int(total_length / len(valid_string_list))

    for string in valid_string_list:
        if len(string) > average_length:
            true_strings.append(string)


    return true_strings, average_length, total_length

if __name__ == "__main__":
    string_list = ["cat","dragon","music","wine","stars","pilgrim",
                   "missisipi",
                   ]

    result = string_length(string_list)

    print(f"Total length of strings: {result[2]}")
    print(f"Average length of strings: {result[1]}")
    print(f"Filtered list: \n{result[0]}")


