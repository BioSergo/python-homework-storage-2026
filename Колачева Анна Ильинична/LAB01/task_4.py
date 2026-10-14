#!/usr/bin/env python3

import string

ALL_PUNCT = string.punctuation + "«»—…"
RUS_ALPH = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DICT_AL = { 
    'а':'01', 'б':'02', 'в':'03', 'г':'04', 'д':'05',
    'е':'06', 'ё':'07', 'ж':'08', 'з':'09', 'и':'10',
    'й':'11', 'к':'12', 'л':'13', 'м':'14', 'н':'15',
    'о':'16', 'п':'17', 'р':'18', 'с':'19', 'т':'20',
    'у':'21', 'ф':'22', 'х':'23', 'ц':'24', 'ч':'25',
    'ш':'26', 'щ':'27', 'ъ':'28', 'ы':'29', 'ь':'30',
    'э':'31', 'ю':'32', 'я':'33'
            }

DICT_NUM = { b: n for n, b in DICT_AL.items()}


if __name__ == "__main__":

    while True:
        user_str = input('Введите фразу для шифравания на русском языке или числовую последовательность для дешифровки\n')
       
        clean_str = user_str.replace(" ", "").lower()
        clean_str = ''.join(el for el in clean_str if el not in ALL_PUNCT)

        if not (clean_str.isdigit() or clean_str.isalpha()):
            print('Получилась какая то каша, слова должны состоять ТОЛЬКО из Русских букв или ТОЛЬКО из чисел, давай попробуем ещё раз!\n')
            continue

        elif clean_str.isalpha() and any(el not in RUS_ALPH for el in clean_str):
            print('Как у нас затесался другой язык, кроме русского? А ну ка ещё раз!\n')
            continue

        elif clean_str.isalpha():
            res = []

            for bukva in user_str.lower():
                if bukva in DICT_AL:
                    res.append(DICT_AL[bukva])
                else:
                    res.append(bukva)

            result = ''.join(res)
            print(f'Вот результат шифрования вашей фразы в числовую последовательность: {result}\n')

        else:
            if len(clean_str) % 2 != 0:
                print('Циферок либо больше, либо меньше на одну чем надо!')
                continue

            res_n = []
            i = 0
            while i < len(user_str.lower()):
                par_fig = user_str[i:i+2]

                if par_fig in DICT_NUM:
                    res_n.append(DICT_NUM[par_fig])
                    i += 2
                else:
                    res_n.append(par_fig[0])
                    i += 1
            result_n = ''.join(res_n)
            print(f'Вот результат дешифрования числовой последовательности в буквенную: {result_n}')
        break
