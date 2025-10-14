rows_of_the_field = int(input())
field = []
attacked_list = []
damage_ship = []

for _ in range(rows_of_the_field):
    field += [list((map(int, input().split())))]

attacked = input().split()
for data in attacked:
    attacked_list.extend(data.split("-"))
    attacked_list = list(map(int, attacked_list))

for data_attack in range(0, len(attacked_list), 2):
    row = int(attacked_list[data_attack])
    column = int(attacked_list[data_attack + 1])
    if field[row][column] > 0:
        field[row][column] -= 1
        if field[row][column] == 0:
            damage_ship.append(1)

print(sum(damage_ship))
