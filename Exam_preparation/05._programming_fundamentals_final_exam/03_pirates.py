def plunder(def_command: list, def_targets: dict) -> dict:
    town, people, def_gold = def_command[1], int(def_command[2]), int(def_command[3])
    if (def_targets[town][0] > people) and (def_targets[town][1] > def_gold):
        def_targets[town][0] -= people
        def_targets[town][1] -= def_gold
        print(f"{town} plundered! {def_gold} gold stolen, {people} citizens killed.")
        return def_targets
    amount_people = def_targets[town][0] if def_targets[town][0] <= people else people
    amount_gold = def_targets[town][1] if def_targets[town][1] <= def_gold else def_gold
    print(f"{town} plundered! {amount_gold} gold stolen, {amount_people} citizens killed.")
    print(f"{town} has been wiped off the map!")
    del def_targets[town]
    return def_targets


def prosper(def_command: list, def_targets: dict) -> dict:
    town, def_gold = def_command[1], int(def_command[2])
    if def_gold < 0 :
        print(f"Gold added cannot be a negative number!")
        return def_targets
    def_targets[town][1] += def_gold
    print(f"{def_gold} gold added to the city treasury. {town} now has {def_targets[town][1]} gold.")
    return def_targets


targets = {}

while True:
    command = input().split("||")
    action = command[0]
    if action == "Sail":
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in targets.keys():
        targets[city] = [population, gold]
    else:
        targets[city][0] += population
        targets[city][1] += gold

while True:
    command = input().split("=>")
    action = command[0]
    if action == "End":
        break
    elif action == "Plunder":
        targets = plunder(command, targets)
    elif action == "Prosper":
        targets = prosper(command, targets)

count = len(targets.keys())

if not targets:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for town, data in targets.items():
        print(f"{town} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
