count_decoration = int(input())
days_to_Christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
ornament_spirit = 5
skirt_spirit = 3
garland_spirit = 10
lights_spirit = 17
total_price = 0
total_spirit = 0


for day in range(1, days_to_Christmas+1):
    if day % 11 == 0:
        count_decoration += 2
    if day % 2 == 0:
        total_spirit += ornament_spirit
        total_price += ornament_set * count_decoration
    if day % 3 == 0:
        total_spirit += skirt_spirit + garland_spirit
        total_price += (tree_skirt * count_decoration) + (tree_garland * count_decoration)
    if day % 5 == 0:
        total_spirit += lights_spirit
        total_price += tree_lights * count_decoration
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_price += tree_skirt + tree_garland + tree_lights

if days_to_Christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_price:.0f}")
print(f"Total spirit: {total_spirit:.0f}")
