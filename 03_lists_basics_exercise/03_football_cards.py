team_a = list(f"A-{index}" for index in range(1, 12))
team_b = list(f"B-{index}" for index in range(1, 12))
terminate_flag = False

red_cards = input()
red_cards_list = red_cards.split()

for data in red_cards_list:
    if data in team_a:
        team_a.remove(data)
        if len(team_a) < 7:
            terminate_flag = True
            break
    elif data in team_b:
        team_b.remove(data)
        if len(team_b) < 7:
            terminate_flag = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if terminate_flag:
    print("Game was terminated")
