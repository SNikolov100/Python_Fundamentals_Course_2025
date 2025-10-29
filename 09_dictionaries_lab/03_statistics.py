new_products = {}

while True:
    command = input()
    if command == "statistics":
        break
    command = command.split(": ")
    product, quantity = command[0], int(command[1])
    if product in new_products:
        new_products[product] += quantity
    else:
        new_products[product] = quantity

count_all_products = len(new_products.keys())
sum_all_quantities = sum(new_products.values())
print("Products in stock:")
for product, quantity in new_products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")