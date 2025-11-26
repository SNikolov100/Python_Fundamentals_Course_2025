import re

demons_list = re.split(r",\s*", input())
pattern_for_name = r"[^0-9\+\-\*\/]"
pattern_for_digit = r"[+-]?\d+(?:\.\d+)?"
pattern_for_multi_divide = r"[\*\/]"
demons_dict = {}

for demons in demons_list:
    if not demons:
        continue
    damage_points = 0
    health = 0
    result_digit = re.findall(pattern_for_digit, demons)
    demon_without_numbers = re.sub(pattern_for_digit, "", demons)
    char_for_name = re.findall(pattern_for_name, demon_without_numbers)
    for char in char_for_name:
        if char:
            health += ord(char)
    result_multi_divide = re.findall(pattern_for_multi_divide, demons)
    for digit in result_digit:
        damage_points += float(digit)
    for action in result_multi_divide:
        if action == "*":
            damage_points = damage_points * 2
        else:
            damage_points = damage_points / 2
    demons_dict[demons] = [health, damage_points]

for demon in sorted(demons_dict.keys()):
    health, damage = demons_dict[demon]
    if health == 0:
        continue
    if " " in demon:
        continue
    print(f"{demon} - {health} health, {damage:.2f} damage")
