#!/usr/bin/env python3

PRODUCTS = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]
def shop():
    """
    Функция, которая возвращает отсортированный словарь с расчитаной финальной ценой.

    :return: Отсортированный список словарей с final_price
    :rtype: list[dict]
    """

    price_with_discount = list(map
                               (lambda x:{**x, "final_price": x["price"] * ((100 - x["discount"]) / 100)}, PRODUCTS))

    low_to_high_price = sorted(price_with_discount, key=lambda x: x["final_price"])

    return low_to_high_price

if __name__ == '__main__':
    results = shop()
    for item in results:
        print(item)
