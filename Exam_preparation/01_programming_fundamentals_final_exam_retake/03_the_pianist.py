def add_pieces(current_command: list, current_pieces: dict) -> dict:
    piece, composer, key = current_command[1], current_command[2], current_command[3]
    for current_piece, current_composer in current_pieces.items():
        if current_piece == piece:
            print(f"{piece} is already in the collection!")
            return pieces
    pieces[piece] = [composer, key]
    print(f"{piece} by {composer} in {key} added to the collection!")
    return pieces


def remove_pieces(current_command: list, current_pieces: dict) -> dict:
    piece = current_command[1]
    for current_piece in current_pieces.keys():
        if piece in current_piece:
            print(f"Successfully removed {piece}!")
            del current_pieces[piece]
            return current_pieces
    print(f"Invalid operation! {piece} does not exist in the collection.")
    return current_pieces


def change_key_pieces(current_command: list, current_pieces: dict) -> dict:
    piece, new_key = current_command[1], current_command[2]
    for current_piece, info in current_pieces.items():
        if piece in current_piece:
            current_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
            return current_pieces
    print(f"Invalid operation! {piece} does not exist in the collection.")
    return current_pieces


number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    action = command[0]
    if action == "Add":
        pieces = add_pieces(command, pieces)
    elif action == "Remove":
        pieces = remove_pieces(command, pieces)
    elif action == "ChangeKey":
        pieces = change_key_pieces(command, pieces)

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")
