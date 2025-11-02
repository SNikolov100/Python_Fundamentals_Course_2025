products_dictionary = {}

while True:
    command = input()
    if command == "buy":
        break
    information_about_product = command.split()
    name = information_about_product[0]
    price = float(information_about_product[1])
    quantity = float(information_about_product[2])
    if name not in products_dictionary.keys():
        products_dictionary[name] = [0, 0]
    products_dictionary[name][0] = price
    products_dictionary[name][1] += quantity

for product_name, price in products_dictionary.items():
    print(f"{product_name} -> {(price[0] * price[1]):.2f}")

