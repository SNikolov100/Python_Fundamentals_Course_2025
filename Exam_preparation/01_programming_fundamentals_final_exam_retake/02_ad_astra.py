import re

text_string = input()
pattern = r"([#|])([a-zA-Z]+(?: [a-zA-Z]+)*)\1(\d{2}/\d{2}/\d{2})\1(0|[1-9]\d{0,3}|10000)\1"
total_calories = 0
info_foods = re.finditer(pattern, text_string)

for info in info_foods:
    calories = info.group(4)
    total_calories += int(calories)
days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")

info_foods = re.finditer(pattern, text_string)
for info in info_foods:
    item_name = info.group(2)
    expiration_date = info.group(3)
    calories = info.group(4)
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")