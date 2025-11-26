def drive(current_car: str, add_distance: int, need_fuel: int, current_info_car: dict) -> dict:
    if current_car in current_info_car:
        if need_fuel > current_info_car[current_car][1]:
            print("Not enough fuel to make that ride")
            return current_info_car
        current_info_car[current_car][1] -= need_fuel
        current_info_car[current_car][0] += add_distance
        print(f"{current_car} driven for {add_distance} kilometers. {need_fuel} liters of fuel consumed.")
        if current_info_car[current_car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del current_info_car[current_car]
    return current_info_car


def refuel(current_car: str, add_fuel: int, current_info_car: dict) -> dict:
    if current_car in current_info_car:
        start_fuel = current_info_car[current_car][1]
        current_info_car[current_car][1] += add_fuel
        refueled = add_fuel
        if current_info_car[current_car][1] > 75:
            refueled = 75 - start_fuel
            current_info_car[current_car][1] = 75

        print(f"{current_car} refueled with {refueled} liters")
    return current_info_car


def revert(current_car: str, decrease_miles: int, current_info_car: dict) -> dict:
    if current_car in current_info_car:
        current_info_car[current_car][0] -= decrease_miles
        if current_info_car[current_car][0] < 10000:
            current_info_car[current_car][0] = 10000
            return current_info_car
        print(f"{current_car} mileage decreased by {decrease_miles} kilometers")
    return current_info_car


number_of_cars = int(input())

info_car = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    info_car[car] = [int(mileage), int(fuel)]

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    car = command[1]
    if command[0] == "Drive":
        distance, fuel = int(command[2]), int(command[3])
        info_car = drive(car,distance, fuel, info_car)
    elif command[0] == "Refuel":
        fuel = int(command[2])
        info_car = refuel(car, fuel, info_car)
    elif command[0] == "Revert":
        miles = int(command[2])
        info_car = revert(car, miles, info_car)

for car, info in info_car.items():
    mileage, fuel = info[0], info[1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
