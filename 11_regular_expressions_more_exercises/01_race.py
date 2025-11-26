import re

drivers = input().split(", ")
ranking = {}
pattern_for_digits = r"\d"
pattern_for_names = r"[a-zA-Z]+"

while True:
    name = ""
    distance = 0
    command = input()
    if command == "end of race":
        break
    names = re.findall(pattern_for_names, command)
    for letter in names:
        name += letter
    digits = re.finditer(pattern_for_digits, command)
    for digit in digits:
        distance += int(digit.group())
    if name in drivers:
        if name not in ranking.keys():
            ranking[name] = distance
        else:
            ranking[name] += distance

sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_ranking[0][0]}")
print(f"2nd place: {sorted_ranking[1][0]}")
print(f"3rd place: {sorted_ranking[2][0]}")
