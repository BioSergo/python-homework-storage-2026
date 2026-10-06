#!/usr/bin/env python3

def recursive(n):

    if n == 1:
        return 1

    return n*recursive(n-1)

def iterative(n):

    for a in range(1,n):
        n *= a
    return n

if __name__ == '__main__':

    while True:
        n = input("Введите челое число:\n")
        if n.isdigit():
            true_num = int(n)
            break
        else:
            print("Введите целое число!")

result_recursive = recursive(true_num)
result_iterative = iterative(true_num)
print(f"Факториал через функцию рекурсивным методом: {result_recursive}")
print(f"Факториал через функцию итеративным способом: {result_iterative}")




