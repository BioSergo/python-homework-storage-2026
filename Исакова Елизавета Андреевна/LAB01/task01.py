DELIMITER = ','

def check_for_distinctness(entrance):
    lst_entrance = entrance.split(DELIMITER)
    lst_entrance = [x.strip() for x in lst_entrance]
    set_lst_entrance = set(lst_entrance)
    if len(lst_entrance) != len(set_lst_entrance):
        duplicates = [y for y in set_lst_entrance if lst_entrance.count(y) > 1]
        return f'Не все числа в последовательности различны, повторяющиеся: {DELIMITER.join(duplicates)}'
    else:
        return 'Все числа в последовательности различны'


if __name__ == "__main__":
    while True:
        sequence = input('Введите последовательность чисел через запятую:\n')

        if not sequence:
            print('Вы ничего не ввели, попробуйте еще раз!')
            continue

        elements_sequence = sequence.replace(DELIMITER,' ').split()

        all_numbers = True
        for number in elements_sequence:
            try:
                the_correct_number = float(number)
            except ValueError:
                all_numbers = False
                print('Вы ввели не число, попробуйте еще раз!')
                break

        if not all_numbers:
            continue

        if DELIMITER not in sequence:
            print('Вы ввели числа не через запятую, попробуйте еще раз!')
            continue

        print(check_for_distinctness(sequence))
        break
