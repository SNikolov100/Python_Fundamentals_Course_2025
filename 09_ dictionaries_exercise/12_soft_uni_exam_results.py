exam_log = {}
is_banned = False
counter_people = {}

while True:
    command = input().split("-")
    if command[0] == "exam finished":
        break
    user_name = command[0]
    if len(command) == 3:
        language = command[1]
        points = int(command[2])
    else:
        if "banned" not in exam_log.keys():
            is_banned = True
            exam_log["banned"] = []
        exam_log["banned"].append(user_name)
        continue
    if language not in exam_log:
        exam_log[language] = {}
        counter_people[language] = 0
    counter_people[language] += 1
    if user_name in exam_log[language].keys():
        if points < exam_log[language][user_name]:
            continue
    exam_log[language][user_name] = points

new_exam_log_without_banned = exam_log.copy()
if is_banned:
    del new_exam_log_without_banned["banned"]

if new_exam_log_without_banned:
    print("Results:")
    for language, names in new_exam_log_without_banned.items():
        for name, points in names.items():
            if is_banned:
                for banned_names in exam_log["banned"]:
                    if name == banned_names:
                        continue
                    print(f"{name} | {points}")
            else:
                print(f"{name} | {points}")
    print("Submissions:")
    for language in new_exam_log_without_banned.keys():
        print(f"{language} - {counter_people[language]}")


