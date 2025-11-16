players_pool = {}
players_vs_players = {}
total_skill = {}

while True:
    command = input()
    if command == "Season end":
        break
    elif "->" in command:
        command = command.split(" -> ")
        player, position, skill = command[0], command[1], int(command[2])
        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player][position] = skill
        if skill > players_pool[player][position]:
            players_pool[player][position] = skill
    else:
        command = command.split(" vs ")
        player_1, player_2 = command[0], command[1]
        if player_1 not in players_pool or player_2 not in players_pool:
            continue
        players_vs_players[player_1] = player_2

for player, position_skill in players_pool.items():
    if player not in total_skill:
        total_skill[player] = 0
    for position, skill in position_skill.items():
        total_skill[player] += skill


for player_one, player_two in players_vs_players.items():
    for position, skill in players_pool[player_one].items():
        if position in players_pool[player_two] and player_one in total_skill and player_two in total_skill:
            if total_skill[player_one] > total_skill[player_two]:
                del total_skill[player_two]
            elif total_skill[player_one] < total_skill[player_two]:
                del total_skill[player_one]

for player, total in sorted(total_skill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {total} skill")
    for position, skill in sorted(players_pool[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
