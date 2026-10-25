def product_market(**kwargs):
    print(kwargs)

    return 0

product = [{"name": "Mouse", "price": 2490, "discount": 15},
           {"name": "Keyboard", "price": 5490, "discount": 0},
           {"name": "Monitor", "price": 27990, "discount": 25}
           ]

listing = product_market(name= 'Laptop',price = 89888, discount = 20)



