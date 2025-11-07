user_name = input().split(", ")
is_valid = True

for data in user_name:
    if not 3 <= len(data) <= 16:
        is_valid = False
    elif not data.isalnum() and not ("-" in data) and not ("_" in data):
        is_valid = False
    elif " " in data:
        is_valid = False

    if is_valid:
        print(data)
    is_valid = True