import re

coordinates = {}
encrypted_messages = input()
pattern = r"([*^]+)([A-Za-z ]{6,})([*^]+)[^A-Za-z0-9]*\+(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\+"

coordinate_from_pattern = re.finditer(pattern, encrypted_messages, re.IGNORECASE)

for data in coordinate_from_pattern:
    coordinates[data.group(2)] = [data.group(4), data.group(5)]
if not coordinates:
    print(f"No valid artifacts found.")
else:
    for place, info in coordinates.items():
        print(f"Found {place} at coordinates {info[0]},{info[1]}.")
