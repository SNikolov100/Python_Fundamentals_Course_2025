def jump_hearts(houses, index: int, new_inx: int, house_counter: int):
    new_inx += index
    if new_inx >= len(houses):
        new_inx = 0
    if houses[new_inx] == 0:
        print(f"Place {new_inx} already had Valentine's day.")
    else:
        houses[new_inx] -= 2
        if houses[new_inx] == 0:
            print(f"Place {new_inx} has Valentine's day.")
            house_counter += 1
    return houses, new_inx, house_counter


neighborhood = list(map(int, input().split("@")))
house_index = 0
house_count = 0

while True:
    command = input()
    if command == "Love!":
        break
    command = command.split()
    length = int(command[1])
    neighborhood, house_index, house_count = jump_hearts(neighborhood, length, house_index, house_count)

print(f"Cupid's last position was {house_index}.")
successful_mission = set(neighborhood)
if len(successful_mission) == 1 and neighborhood[0] == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - house_count} places.")
