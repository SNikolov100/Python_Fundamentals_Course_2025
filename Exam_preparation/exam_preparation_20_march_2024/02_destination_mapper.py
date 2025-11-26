import re

travel_points = 0
locations = []
places = input()
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"

valid_location = re.finditer(pattern, places)
for location in valid_location:
    locations.append(location.group(2))

for locate in locations:
    travel_points += len(locate)

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")
