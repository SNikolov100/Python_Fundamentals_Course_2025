number_of_users = int(input())
parking = {}

for _ in range(number_of_users):
    validate_park_place = input().split()
    registration = validate_park_place[0]
    username = validate_park_place[1]
    if registration == "register":
        license_plate_number = validate_park_place[2]
        if username not in parking:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
            continue
        print(f"ERROR: already registered with plate number {license_plate_number}")
    elif registration == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
            continue
        print(f"{username} unregistered successfully")
        del parking[username]

for username, validate_park_place in parking.items():
    print(f"{username} => {validate_park_place}")

