def side_search(c1, c2, h):
    if c1 == 0:
        result1 = (h**2 - c2**2) ** 0.5
        return f'Первый катет - {result1}'
    elif c2 == 0:
        result1 = (h**2 - c1**2) ** 0.5
        return f'Второй катет - {result1}'
    elif h == 0:
        result1 = (c1**2 + c2**2) ** 0.5
        return f'Гипотенуза - {result1}'
    else:
        return 'Все стороны известны'


if __name__ == '__main__':
    cathetus_1_str = input('Введите значение одного катета (или Enter если неизвестно)\n')
    cathetus_2_str = input('Введите значение второго катета (или Enter если неизвестно)\n')
    hypotenuse_str = input('Введите значение гипотенузы (или Enter если неизвестно)\n')

    cathetus_1 = 0.0
    cathetus_2 = 0.0
    hypotenuse = 0.0

    is_valid_input = True
    try:
        if cathetus_1_str:
            cathetus_1 = float(cathetus_1_str)
        if cathetus_2_str:
            cathetus_2 = float(cathetus_2_str)
        if hypotenuse_str:
            hypotenuse = float(hypotenuse_str)
    except ValueError:
        print('Ошибка! Введите число или просто Enter')
        is_valid_input = False

    if is_valid_input:
        known_sides = 0
        if cathetus_1 != 0:
            known_sides += 1
        if cathetus_2 != 0:
            known_sides += 1
        if hypotenuse != 0:
            known_sides += 1

        if known_sides == 0:
            print('Вы ничего не ввели!')
        elif known_sides == 1:
            print('Недостаточно данных! Для расчета необходимо знать как минимум две стороны')
        else:
            result = side_search(cathetus_1, cathetus_2, hypotenuse)
            print(result)
