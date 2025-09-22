number_of_pour = int(input())

capacity_tank = 255

for _ in range(number_of_pour):
    enter_liters = int(input())
    if capacity_tank >= enter_liters:
        capacity_tank -= enter_liters
    else:
        print("Insufficient capacity!")
        continue

print(255 - capacity_tank)
