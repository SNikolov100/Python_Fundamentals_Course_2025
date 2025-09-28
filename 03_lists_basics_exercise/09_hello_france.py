purchases = input().split("|")
budget = float(input())
profit = 0
profit_list = []
total_sum = 0
price_list = []

for purchase in purchases:
    type_item, price = purchase.split("->")
    price = float(price)
    if price <= budget:
        if (type_item == "Clothes" and 0 <= price <= 50) or \
                (type_item == "Shoes" and 0 <= price <= 35) or\
                (type_item == "Accessories" and 0 <= price <= 20.50):

            budget -= price
            price_list.append(price * 1.4)
            profit_list.append(price * 0.4)

profit = sum(profit_list)
price = sum(price_list)
print(" ".join(f"{data_price_list:.2f}" for data_price_list in price_list))
print(f"Profit: {profit:.2f}")
if (price + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")





