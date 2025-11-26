import re

income = 0

while True:
    command = input()
    if command == "end of shift":
        break
    pattern_customer = r"%([A-Z][a-z]+)%"
    pattern_product = r"<(\w+)>"
    product_count_price = r"\|([0-9]+)\b\|[a-zA-Z]*([0-9]+.[0-9]*)\$"
    temp_value = re.findall(pattern_customer, command)
    if not temp_value:
        continue
    customer_name = temp_value[0]
    temp_value = re.findall(pattern_product, command)
    if not temp_value:
        continue
    product = temp_value[0]
    temp_value = re.findall(product_count_price, command)
    if not temp_value:
        continue
    count = temp_value[0][0]
    price = temp_value[0][1]
    total_price = int(count) * float(price)
    print(f"{customer_name}: {product} - {total_price:.2f}")
    income += total_price

print(f"Total income: {income:.2f}")