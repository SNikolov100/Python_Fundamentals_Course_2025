def cast_spell(current_command: list, current_heroes:  dict) -> dict:
    name, mp_needed, spell_name = current_command[1], int(current_command[2]), current_command[3]
    current_mana = current_heroes[name][1]
    if mp_needed <= current_mana:
        current_heroes[name][1] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {current_heroes[name][1]} MP!")
        return current_heroes
    print(f"{name} does not have enough MP to cast {spell_name}!")
    return current_heroes


def take_damage(current_command: list, current_heroes:  dict) -> dict:
    name, damage, attacker = current_command[1], int(current_command[2]), current_command[3]
    current_heroes[name][0] -= damage
    if current_heroes[name][0] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {current_heroes[name][0]} HP left!")
        return current_heroes
    print(f"{name} has been killed by {attacker}!")
    del current_heroes[name]
    return current_heroes


def recharge(current_command: list, current_heroes:  dict) -> dict:
    name, amount = current_command[1], int(current_command[2])
    amount_recovered = amount
    if (amount + current_heroes[name][1]) > 200:
        amount_recovered = 200 - current_heroes[name][1]
        current_heroes[name][1] = 200
    else:
        current_heroes[name][1] += amount
    print(f"{name} recharged for {amount_recovered} MP!")
    return current_heroes


def heal(current_command: list, current_heroes:  dict) -> dict:
    name, amount = current_command[1], int(current_command[2])
    amount_recovered = amount
    if (amount + current_heroes[name][0]) > 100:
        amount_recovered = 100 - current_heroes[name][0]
        current_heroes[name][0] = 100
    else:
        current_heroes[name][0] += amount
    print(f"{name} healed for {amount_recovered} HP!")
    return current_heroes


number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    hero_name, health, mana = input().split()
    health, mana = int(health), int(mana)
    health = 100 if health > 100 else health
    mana = 200 if mana > 200 else mana
    heroes[hero_name] = [health, mana]

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break
    elif action == "CastSpell":
        heroes = cast_spell(command, heroes)
    elif action == "TakeDamage":
        heroes = take_damage(command, heroes)
    elif action == "Recharge":
        heroes = recharge(command, heroes)
    elif action == "Heal":
        heroes = heal(command, heroes)

for hero, data in heroes.items():
    print(hero)
    print(f"\tHP: {data[0]}")
    print(f"\tMP: {data[1]}")


