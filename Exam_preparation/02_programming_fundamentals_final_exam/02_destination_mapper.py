import re

string_of_places = input()
pattern = r"([=/])([A-Z][a-zA-Z]{2,})\1"
place_list = []
travel_points = 0
valid_places = re.findall(pattern, string_of_places)
for place in valid_places:
    travel_points += len(place[1])
    place_list.append((place[1]))
print(f"Destinations: {', '.join(place_list)}")
print(f"Travel Points: {travel_points}")
