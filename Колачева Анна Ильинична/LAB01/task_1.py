#!/usr/bin/env python3

DELIMITER = ";"
def proverka(var_l: list) -> None:
    if len(var_l) == len(set(var_l)):
        print("Cool!")
    else:
        print("Sorry, but no","\U0001F641" )

    for i in set(var_l):
        if (coun := var_l.count(i)) > 1:
            print(f'{i} appears in the sequence {coun} times')
            print('if you want to try one again restart the script')

def check_if_only_num(var_l: list) -> bool:
    try:
        for n in var_l:
            if not n.strip(): 
                raise ValueError
            float(n.strip())
        return True
    except ValueError:
        print(f'The sequence contains not only numbers or you fogot a "{DELIMITER}" (or you write float on wrong way )')
        return False


if __name__ == "__main__":
    var: str = input(f'Enter the sequence of numbers separated by "{DELIMITER}" (if you want to add some floats, please write them like (1.5)):\n')
    while True:
        var_l: list[str] = var.split(DELIMITER)

        if check_if_only_num(var_l):
            proverka(var_l)
            break
        else:
            var = input("Try one more!\n")
 
