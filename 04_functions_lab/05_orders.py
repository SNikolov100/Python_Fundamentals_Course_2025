def orders(product, quantity) ->float:
    if product == "coffee":
        return coffee_price * quantity
    if product == "coke":
        return coke_price * quantity
    if product == "water":
        return water_price * quantity
    if product == "snacks":
        return snacks_price * quantity


coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

input_product = input()
quantity_of_product = int(input())

result = orders(input_product, quantity_of_product)
print(f"{result:.2f}")
