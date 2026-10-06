#!/usr/bin/env python3


def multiplexer(arg):

    multi_arg = 1
    info_arg_list = []

    for argument in arg:
        if isinstance(argument, int):
            multi_arg *= argument
        else:
            info = type(argument)
            info_arg = (argument, info)
            info_arg_list.append(info_arg)

    return multi_arg, info_arg_list

if __name__ == '__main__':

    arguments = [4,2,1,2,4.5,'hello','now',['wow'],(2,'wow')]

    multi_result, wrong_arg_types = multiplexer(arguments)
    print(f"Multiplying result:\n{multi_result}")

    for wrong_arg in wrong_arg_types:
        info1, info2 = wrong_arg

        print(f"Argument:\n{info1} is {info2}")






