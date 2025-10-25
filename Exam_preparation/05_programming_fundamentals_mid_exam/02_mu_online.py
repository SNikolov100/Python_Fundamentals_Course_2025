def potion(value_pot: int, health_pot: int) -> int:
    old_health = health_pot
    health_pot += value_pot
    if health_pot > 100:
        health_pot = 100
    print(f"You healed for {health_pot - old_health} hp.")
    print(f"Current health: {health_pot} hp.")
    return health_pot


def chest(bitcoins_chest: int, value_chest: int) -> int:
    print(f"You found {value_chest} bitcoins.")
    bitcoins_chest += value_chest
    return bitcoins_chest


def monster(command_current: str, attack: int, health_current: int, is_dead_current: bool):
    health_current -= attack
    if health_current <= 0:
        is_dead_current = True
    return health_current, is_dead_current


input_command = input().split("|")
count_room = 0
is_dead = False
bitcoins = 0
health = 100
index = 0
while count_room < len(input_command):
    count_room += 1
    key = input_command[index].split()
    command = key[0]
    value = int(key[1])
    index += 1
    if command == "potion":
        health = potion(value, health)
    elif command == "chest":
        bitcoins = chest(bitcoins, value)
    else:
        health, is_dead = monster(command, value, health, is_dead)
        if is_dead:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_room}")
            break
        print(f"You slayed {command}.")

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
