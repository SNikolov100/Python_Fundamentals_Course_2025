number_dragons = int(input())
type_name = {}
type_statistics = {}

for _ in range(number_dragons):
    type_dragon, name, damage, health, armor = input().split()
    damage = 45 if damage == "null" else int(damage)
    health = 250 if health == "null" else int(health)
    armor = 10 if armor == "null" else int(armor)
    if type_dragon not in type_name:
        type_name[type_dragon] = {}
    type_name[type_dragon][name] = [damage, health, armor]


for type_dragon, names in type_name.items():
    damage, health, armor = 0, 0, 0
    counter_names = 0
    for name, info in names.items():
        counter_names += 1
        damage += info[0]
        health += info[1]
        armor += info[2]
    average_damage = damage / counter_names
    average_health = health / counter_names
    average_armor = armor / counter_names
    if type_dragon not in type_statistics:
        type_statistics[type_dragon] = []
    type_statistics[type_dragon] = [average_damage, average_health, average_armor]


for type_dragon, names in type_name.items():
    type_name[type_dragon] = dict(sorted(type_name[type_dragon].items(), key=lambda x: x[0]))

for type_dragon, names in type_name.items():
    print(f"{type_dragon}::({type_statistics[type_dragon][0]:.2f}/{type_statistics[type_dragon][1]:.2f}/{type_statistics[type_dragon][2]:.2f})")
    for name, info in names.items():
        print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")
