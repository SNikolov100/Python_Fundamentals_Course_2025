def cast_spell(def_command: list, def_heroes: dict) -> dict:
    name, mp_needed, spell_name = def_command[1], int(def_command[2]), def_command[3]
    if def_heroes[name][1] < mp_needed:
        print(f"{name} does not have enough MP to cast {spell_name}!")
        return def_heroes
    def_heroes[name][1] -= mp_needed
    print(f"{name} has successfully cast {spell_name} and now has { def_heroes[name][1]} MP!")
    return def_heroes


def take_damage(def_command: list, def_heroes: dict) -> dict:
    name, damage, attacker = def_command[1], int(def_command[2]), def_command[3]
    def_heroes[name][0] -= damage
    if def_heroes[name][0] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {def_heroes[name][0]} HP left!")
        return def_heroes
    print(f"{name} has been killed by {attacker}!")
    del def_heroes[name]
    return def_heroes


def recharge(def_command: list, def_heroes: dict) -> dict:
    name, amount = def_command[1], int(def_command[2])
    initial_mana = def_heroes[name][1]
    def_heroes[name][1] += amount
    if def_heroes[name][1] > 200:
        amount = 200 - initial_mana
        def_heroes[name][1] = 200
    print(f"{name} recharged for {amount} MP!")
    return def_heroes


def heal(def_command: list, def_heroes: dict) -> dict:
    name, amount = def_command[1], int(def_command[2])
    initial_hp = def_heroes[name][0]
    def_heroes[name][0] += amount
    if def_heroes[name][0] > 100:
        amount = 100 - initial_hp
        def_heroes[name][0] = 100
    print(f"{name} healed for {amount} HP!")
    return def_heroes


number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    hp = 100 if hp > 100 else hp
    mp = 200 if mp > 200 else mp
    heroes[hero_name] = [hp, mp]
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

for hero_name, info in heroes.items():
    current_hp = info[0]
    current_mp = info[1]
    print(hero_name)
    print(f"  HP: {current_hp}")
    print(f"  MP: {current_mp}")