import re

pattern = r">>([a-z]+)<<(\d+\.?\d+)!(\d+)"
total_money = 0
furniture_list = []

while True:
    command = input()
    if command == "Purchase":
        break
    furniture_info = re.search(pattern, command, re.IGNORECASE)
    if furniture_info:
        furniture, price, quantity = furniture_info.group(1), float(furniture_info.group(2)), int(furniture_info.group(3))
        furniture_list.append(furniture)
        total_money += price * quantity

print("Bought furniture:")
for data in furniture_list:
    print(data)
print(f"Total money spend: {total_money:.2f}")
