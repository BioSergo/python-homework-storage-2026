#!/usr/bin/env python3

PRODUCTS = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]


def inputer():
    """
    Функция которая дополняет список продуктов PRODUCTS, пользовательским.

    :return: модифицированный PRODUCTS
    """
    while True:

        name = input(f'Type name of product:\n> ')
        price = int(input(f'Type price of product:\n '))
        discount = int(input(f'Type discount(%) of product:\n '))
        PRODUCTS.append({"name": name, "price": price, "discount": discount})
        anything_else = input(f'Do you want to add another product? (y/n):\n ')
        if anything_else.lower() == "n":
            break

    return PRODUCTS

def shop():
    """
    Функция, которая возвращает отсортированный словарь с расчитаной финальной ценой.

    :return: Отсортированный список словарей с final_price
    """

    price_with_discount = list(map
                               (lambda x:{
                                   **x, "final_price":
                                       x["price"] * ((100 - x["discount"]) / 100)}, PRODUCTS))


    pricing = lambda x: x["final_price"]

    n = len(price_with_discount)

    for i in range(n):
        for j in range(0, n-i-1):
            if pricing(price_with_discount[j]) > pricing(price_with_discount[j+1]):
                price_with_discount[j], price_with_discount[j+1] = price_with_discount[j+1], price_with_discount[j]

    return price_with_discount

if __name__ == '__main__':
    inputer()

    results = shop()
    for item in results:
        print(item)


