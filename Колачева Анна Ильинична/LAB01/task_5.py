#!/usr/bin/env python3

def v_gip(a,b):
    gip = (a**2 + b**2)**0.5
    return round(gip, 2)

def v_kat(a,c):
    sec_kat = (c**2 - a**2)**0.5
    return round(sec_kat, 2)
def user_input_kat(text):
    while True:
            
            try:
                kat = float(input(text).replace(',','.'))
                break
    
            except ValueError:
                print(f'Это не число, пробуй ещё раз!\n')
    return kat
    

def user_input_gip(text, a):
    while True:
        c = user_input_kat(text)
        if round(c , 3) < round(a , 3):
            print("Гипотенуза должна быть меньше изввестного катета, пробуем снова!\n")
            continue
        else:
            break
    return c 

if __name__ == "__main__":
   a = user_input_kat('Введите известный катет:\n')
    
    what_n =int(input('Если хотите провести расчет по двум катетам введите - 1, если же по катету и гипотенузе - 2:\n'))

    b = None
    c = None

    if what_n == 1:
        b = user_input_kat('Введите второй катет:\n')
        print(f' Гипотенуза в таком треугольнике ровна {v_gip(a,b)}')

    if what_n == 2:
        c = user_input_gip('Введите гипотенузу:\n', a)
        print(f' Второй катет в таком треугольнике ровна {v_kat(a,c)}')
