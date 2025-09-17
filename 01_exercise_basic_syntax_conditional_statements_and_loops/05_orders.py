number_orders = int(input())
price = 0
total_price = 0

for _ in range(number_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price_capsule <= 100.00):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules_per_day <= 2000):
        continue
    price = price_capsule * days * capsules_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")