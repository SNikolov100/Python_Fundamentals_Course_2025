force_log = {}
action = ""
force_user = ""
force_side = ""

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        separate_command = command.split(" | ")
        force_side = separate_command[0]
        force_user = separate_command[1]
        action = "|"
    elif " -> " in command:
        separate_command = command.split(" -> ")
        force_side = separate_command[1]
        force_user = separate_command[0]
        action = "->"

    if action == "|":
        if force_side not in force_log:
            force_log[force_side] = []
        if any(force_user in force_users for force_users in force_log.values()):
            continue
        force_log[force_side].append(force_user)

    if action == "->":
        if force_side not in force_log:
            force_log[force_side] = []
        if any(force_user in force_users for force_users in force_log.values()):
            for force_users in force_log.values():
                if force_user in force_users:
                    force_users.remove(force_user)
        force_log[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for force_side, force_users in force_log.items():
    if len(force_users) > 0 :
        print(f"Side: {force_side}, Members: {len(force_users)}")
        print(*[f"! {force_user}" for force_user in force_users], sep="\n")






