def loot(loot_items: list, items: list) -> list:
    for index_loot in range(1, len(items)):
        if items[index_loot] not in loot_items:
            loot_items.insert(0, items[index_loot])
    return loot_items


def drop(loot_items: list, drop_index: int) -> list:
    if drop_index in range(len(loot_items)):
        move_item = loot_items.pop(drop_index)
        loot_items.append(move_item)
    return loot_items


def steal(loot_items: list, least_count: int) -> list:
    if least_count in range(1, len(loot_items)):
        last_count_items = len(loot_items) - least_count
        print(", ".join(loot_items[last_count_items:]))
        loot_items = loot_items[:last_count_items]
    elif least_count >= len(loot_items):
        print(", ".join(loot_items))
        loot_items = []
    return loot_items


chest_loot = input().split("|")
sum_length = 0

while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    elif action == "Loot":
        chest_loot = loot(chest_loot, command)
    elif action == "Drop":
        index = int(command[1])
        chest_loot = drop(chest_loot, index)
    elif action == "Steal":
        count = int(command[1])
        chest_loot = steal(chest_loot, count)

if not chest_loot:
    print("Failed treasure hunt.")
else:
    for item in chest_loot:
        sum_length += len(item)
    average_gain = sum_length / len(chest_loot)
    print(F"Average treasure gain: {average_gain:.2f} pirate credits.")
