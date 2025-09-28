energy = 100
coins = 100
events = input().split("|")
end_day_flag = False
name_event = ""

for event in events:
    name_event, energy_or_coins = event.split("-")
    energy_or_coins = int(energy_or_coins)
    if name_event == "rest":
        energy += energy_or_coins
        if energy > 100:
            profit_energy = energy_or_coins - (energy - 100)
            energy = 100
        else:
            profit_energy = energy_or_coins
        print(f"You gained {profit_energy} energy.")

        print(f"Current energy: {energy}.")
    elif name_event == "order":
        if (energy - 30) >= 0:
            coins += energy_or_coins
            energy -= 30
            print(f"You earned {energy_or_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if energy_or_coins <= coins:
            coins -= energy_or_coins
            print(f"You bought {name_event}.")
        else:
            end_day_flag = True
            break

if end_day_flag:
    print(f"Closed! Cannot afford {name_event}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
