def receive(current_quantity: int, current_food: str, current_stocks: dict) -> dict:
    if current_quantity <= 0:
        return current_stocks
    if current_food not in current_stocks:
        current_stocks[current_food] = current_quantity
    else:
        current_stocks[current_food] += current_quantity
    return current_stocks


def sell(current_quantity: int, current_food: str, current_stocks: dict, count_sold: int):
    if current_food not in current_stocks:
        print(f"You do not have any {current_food}.")
        return current_stocks, count_sold
    if current_stocks[current_food] >= current_quantity:
        current_stocks[current_food] -= current_quantity
        print(f"You sold {current_quantity} {current_food}.")
        count_sold += current_quantity
        if current_stocks[current_food] == 0:
            del current_stocks[current_food]
        return current_stocks, count_sold
    print(f"There aren't enough {current_food}. You sold the last {current_stocks[current_food]} of them.")
    count_sold += current_stocks[current_food]
    del current_stocks[current_food]
    return current_stocks, count_sold


sold_items = 0
stocks = {}
while True:
    command = input().split()
    if command[0] == "Complete":
        break
    action, quantity, food = command[0], int(command[1]), command[2]
    if action == "Receive":
        stocks = receive(quantity, food, stocks)
    elif action == "Sell":
        stocks, sold_items = sell(quantity, food, stocks, sold_items)

for food, quantity in stocks.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_items} goods")
