level_of_fire = input().split("#")
amount_of_water = int(input())
total_effort = 0
total_fire = 0
put_out_fire = []

for data in level_of_fire:
    effort = 0
    level_fire, need_water = data.split(" = ")
    need_water = int(need_water)

    if need_water > amount_of_water:
        continue

    if (level_fire == "High" and 81 <= need_water <= 125) or \
        (level_fire == "Medium" and 51 <= need_water <= 80) or \
            (level_fire == "Low" and 1 <= need_water <= 50):

        amount_of_water -= need_water
        effort = need_water * 0.25
        total_fire += need_water
        put_out_fire.append(need_water)

    total_effort += effort

print("Cells:")
for data in put_out_fire:
    print(f" - {data}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
