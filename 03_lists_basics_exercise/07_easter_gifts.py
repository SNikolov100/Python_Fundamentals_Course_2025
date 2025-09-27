name_of_gifts = (input())
gifts_list = name_of_gifts.split()
command = ""
command_list = []
max_index = len(gifts_list) - 1
new_gift_list = []

while True:
    command = input()
    command_list = command.split()
    if command == "No Money":
        break

    elif command_list[0] == "OutOfStock":
        gifts_list = ["None" if data == command_list[1] else data for data in gifts_list]

    elif command_list[0] == "Required":
        index_int = int(command_list[2])
        if 0 <= index_int <= max_index:
            gifts_list[index_int] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_list[max_index] = command_list[1]

for data in gifts_list:
    if data != "None":
        new_gift_list.append(data)

print(" ".join(new_gift_list))
