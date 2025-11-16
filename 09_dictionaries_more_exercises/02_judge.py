all_user_name_dict = {}
individual_dict = {}

while True:
    command = input().split(" -> ")
    if command[0] == "no more time":
        break
    username, contest, points = command[0], command[1], int(command[2])

    if contest not in all_user_name_dict.keys():
        all_user_name_dict[contest] = {}
    if username not in all_user_name_dict[contest]:
        all_user_name_dict[contest][username] = points
    if points > all_user_name_dict[contest][username]:
        all_user_name_dict[contest][username] = points

for contest, username_points in all_user_name_dict.items():
    sorted_dict = dict(sorted(username_points.items(), key=lambda x: x[0]))
    sorted_to_points = dict(sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True))
    print(f"{contest}: {len(sorted_to_points)} participants")
    count = 0
    for username, point in sorted_to_points.items():
        count += 1
        print(f"{count}. {username} <::> {point}")
        if username not in individual_dict:
            individual_dict[username] = 0
        individual_dict[username] += point
sorted_username_to_alpha = dict(sorted(individual_dict.items(), key=lambda x: x[0]))
sorted_username_to_all_points = dict(sorted(sorted_username_to_alpha.items(), key=lambda x: x[1], reverse=True))
counter = 0
print("Individual standings:")
for username, point in sorted_username_to_all_points.items():
    counter += 1
    print(f"{counter}. {username} -> {point}")



