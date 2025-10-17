def counter_strike(energy: int, distance: int, count: int, no_energy: bool):
    if energy >= distance:
        energy -= distance
        count += 1
        energy += count if count % 3 == 0 else 0
    else:
        no_energy = True
    return energy, count, no_energy


initial_energy = int(input())
result = ""
count_win = 0
is_no_energy = False

while True:
    command = input()
    if command == "End of battle":
        result = f"Won battles: {count_win}. Energy left: {initial_energy}"
        break
    command = int(command)
    initial_energy, count_win, is_no_energy = counter_strike(initial_energy, command, count_win, is_no_energy)
    if is_no_energy:
        result = f"Not enough energy! Game ends with {count_win} won battles and {initial_energy} energy"
        break

print(result)


