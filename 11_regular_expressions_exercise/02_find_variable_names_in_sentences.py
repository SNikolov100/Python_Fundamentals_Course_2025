import re
result = []
entered_string = input()
pattern = r"(\b_{1})([a-zA-Z0-9]+)\b"

names = re.finditer(pattern, entered_string, re.IGNORECASE)

for name in names:
    result.append(name.group(2))
print(",".join(result))
