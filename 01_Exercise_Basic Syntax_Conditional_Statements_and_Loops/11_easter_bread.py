budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_1l_milk = price_kg_flour * 1.25
price_one_loave = 1 * price_pack_eggs + 1 * price_kg_flour + 0.25 * price_1l_milk
loaves = budget // price_one_loave
max_loaves = int(loaves)
color_eggs = max_loaves * 3

for index in range(1, max_loaves+1):
    if index % 3 == 0:
        color_eggs -= (index - 2)

money_left = budget - (loaves * price_one_loave)

print(f"You made {max_loaves:.0f} loaves of Easter bread! Now you have {color_eggs:.0f} eggs and {money_left:.2f}BGN left.")
