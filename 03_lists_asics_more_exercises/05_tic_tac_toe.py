def win_player(number_one: str) -> str:
    return "First player won" if number_one == "1" else "Second player won"


tic_tac_toe = [input().split() for _ in range(3)]

result = ""

for index in range(3):
    # rows
    if len(set(tic_tac_toe[index])) == 1 and tic_tac_toe[index][0] != "0":
        result = win_player((tic_tac_toe[index][0]))
        break
    # columns
    if tic_tac_toe[0][index] == tic_tac_toe[1][index] == tic_tac_toe[2][index] != "0":
        result = win_player((tic_tac_toe[0][index]))
        break

if result == "":
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] != "0":
        result = win_player(tic_tac_toe[0][0])
    elif tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] != "0":
        result = win_player(tic_tac_toe[0][2])

if result == "":
    print("Draw!")
else:
    print(result)

