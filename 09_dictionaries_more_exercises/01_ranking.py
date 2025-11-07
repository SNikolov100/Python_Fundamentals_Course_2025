valid_contest = {}
final_contest = {}
while True:
    command = input().split(":")
    if command[0] == "end of contests":
        break
    contest = command[0]
    password_for_contest = command[1]
    if contest not in valid_contest.keys():
        valid_contest[contest] = password_for_contest

while True:
    command = input().split("=>")
    if command[0] == "end of submissions":
        break
    contest_check = command[0]
    password = command[1]
    username = command[2]
    points = int(command[3])

    if (contest_check not in valid_contest.keys()) or (password != valid_contest[contest_check]):
        continue
    if username not in final_contest.keys():
        final_contest[username] = {contest_check: points}
        continue
    if contest_check not in final_contest[username]:
        final_contest[username][contest_check] = points
        continue
    if points > final_contest[username][contest_check]:
        final_contest[username][contest_check] = points

total_points = {}
for username, contest in final_contest.items():
    total_points[username] = sum(contest.values())

user = max(total_points, key=total_points.get)
max_total_points = total_points[user]
print(f"Best candidate is {user} with total {max_total_points} points.")
print("Ranking:")

for username in sorted(final_contest.keys()):
    print(f"{username}")
    for contest, points in sorted(final_contest[username].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
