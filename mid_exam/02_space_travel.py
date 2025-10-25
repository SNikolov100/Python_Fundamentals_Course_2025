def travel_years(fuel: int, light_years: int, stop_program: bool):
    if light_years <= fuel:
        fuel -= light_years
        print(f"The spaceship travelled {light_years} light-years.")
        return fuel, stop_program
    stop_program = True
    return fuel, stop_program


def enemy_fight(fuel: int, armor_enemy: int, ammunition: int, stop_program: bool):
    if ammunition >= armor_enemy:
        ammunition -= armor_enemy
        print(f"An enemy with {armor_enemy} armour is defeated.")
        return fuel, ammunition, stop_program
    fuel -= armor_enemy * 2
    if fuel <= 0:
        stop_program = True
        return fuel, ammunition, stop_program
    print(f"An enemy with {armor_enemy} armour is outmaneuvered.")
    return fuel, ammunition, stop_program


def repair_ship(fuel: int , ammunition: int, add_value):
    fuel += add_value
    ammunition += add_value * 2
    print(f"Ammunitions added: {add_value * 2}.")
    print(f"Fuel added: {add_value}.")
    return fuel, ammunition


travel_route_to_titan = input().split("||")
route_list = []
is_stop_program = False
total_fuel = int(input())
total_ammunition = int(input())

for route in travel_route_to_titan:
    if route == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
    route_list = route.split()
    command = route_list[0]
    value = int(route_list[1])
    if command == "Travel":
        total_fuel, is_stop_program = travel_years(total_fuel, value, is_stop_program)
        if is_stop_program:
            print("Mission failed.")
            break
    elif command == "Enemy":
        total_fuel, total_ammunition, is_stop_program = enemy_fight(total_fuel, value, total_ammunition, is_stop_program)
        if is_stop_program:
            print("Mission failed.")
            break
    elif command == "Repair":
        total_fuel, total_ammunition = repair_ship(total_fuel, total_ammunition, value)
