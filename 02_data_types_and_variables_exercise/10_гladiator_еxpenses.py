number_battles_lost = int(input())
expenses = 0
number_repair_shield = 0
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for lost_battle in range(1, number_battles_lost + 1):
    if lost_battle % 2 == 0:
        expenses += helmet_price
    if lost_battle % 3 == 0:
        expenses += sword_price
    if lost_battle % 6 == 0:
        expenses += shield_price
        number_repair_shield += 1
        if number_repair_shield == 2:
            number_repair_shield = 0
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")