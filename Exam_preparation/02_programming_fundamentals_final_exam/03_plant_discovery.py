def rate(current_plant: str, current_rating: float,  current_dictionary: dict) -> dict:
    for plant_key, info_value in current_dictionary.items():
        for current_rarity in info_value:
            if plant_key == current_plant:
                current_dictionary[current_plant][current_rarity].append(current_rating)
    return current_dictionary


def update(current_plant: str, current_new_rarity: int, current_dictionary: dict) -> dict:
    is_change = False
    for plant_key, info_value in current_dictionary.items():
        if current_plant == plant_key:
            for current_rarity in info_value:
                old_key = current_rarity
                is_change = True
    if is_change:
        current_dictionary[current_plant][current_new_rarity] = current_dictionary[current_plant][old_key]
        del(current_dictionary[current_plant][old_key])
    return current_dictionary


def reset(current_plant: str, current_dictionary: dict) -> dict:
    for plant_key, info in current_dictionary.items():
        if plant_key == current_plant:
            for current_rarity in info:
                current_dictionary[current_plant][current_rarity] = []
    return current_dictionary


number = int(input())
plants_dictionary = {}
average_rating = 0

for _ in range(number):
    plants = input().split("<->")
    plant, rarity = plants[0], int(plants[1])
    plants_dictionary[plant] = {rarity: []}
while True:
    command = input().split(":")
    if command[0] == "Exhibition":
        break
    action = command[0]
    action_info = command[1]
    action_info = action_info.split(" - ")
    plant = action_info[0].replace(" ", "")
    if plant not in plants_dictionary:
        print("error")
        continue
    if action == "Rate":
        rating = float(action_info[1])
        plants_dictionary = rate(plant, rating, plants_dictionary)
    elif action == "Update":
        new_rarity = int(action_info[1])
        plants_dictionary = update(plant, new_rarity, plants_dictionary)
    elif action == "Reset":
        plants_dictionary = reset(plant, plants_dictionary)

print(f"Plants for the exhibition:")
for plant, info in plants_dictionary.items():
    average_rating = 0
    for rarity in info:
        if plants_dictionary[plant][rarity]:
            average_rating += sum(plants_dictionary[plant][rarity])/len(plants_dictionary[plant][rarity])
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
