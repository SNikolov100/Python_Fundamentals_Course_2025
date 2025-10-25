days_of_adventure = int(input())
number_of_adventure = int(input())
total_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())
total_water = water_per_person_per_day * number_of_adventure * days_of_adventure
total_food = food_per_person_per_day * number_of_adventure * days_of_adventure
is_no_energy = False

for day in range(1, days_of_adventure + 1):
    daily_energy_loss = float(input())
    total_energy -= daily_energy_loss
    if total_energy <= 0:
        is_no_energy = True
        break
    if day % 2 == 0:
        total_energy += total_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:
        total_energy += total_energy * 0.1
        total_food -= total_food / number_of_adventure

if is_no_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with {total_energy:.2f} energy!")