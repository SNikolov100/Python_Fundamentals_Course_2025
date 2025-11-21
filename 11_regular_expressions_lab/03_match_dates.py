import re

enter_data = input()
pattern = r"(\d{2})(\/|-|.)([A-Z][a-z]{2})\2(\d{4})"

dates = re.finditer(pattern, enter_data)
for info in dates:
    day = info.group(1)
    month = info.group(3)
    year = info.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")