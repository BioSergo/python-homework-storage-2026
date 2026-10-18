def nrev(d):
    nrev_sort = sorted(d)
    return tuple(nrev_sort)

def rev(d):
    rev_sort = sorted(d, reverse=True)
    return tuple(rev_sort)

if __name__ == '__main__':
    while True:
        text = input('Введите числа через запятую:\n').strip()
        parts = text.replace(',', ' ').split()

        try:
            nums = [float(p) for p in parts]
            break
        except ValueError:
            print('Введите именно числа!!\n')

    numbers = [float(p) for p in parts]

    while True:
        print('Введите 1, чтобы отсортировать по возрастанию \n')
        print('Введите 2, чтобы по убыванию\n')
        choice = input('Выбери:\n')

        if choice == '1':
            result = nrev(numbers)
            break
        elif choice == '2':
            result = rev(numbers)
            break
        else:
            print('Впишите числа 1 или 2!\n')

    print('Результат:\n', result)
