import re

single_string = input()
pattern = r"\s(([a-z0-9])([a-z0-9\.\-\_]+)([a-z0-9])@([a-z\-]+)(\.[a-z]+)+)\b"

emails = re.findall(pattern, single_string)
for email in emails:
    print(email[0])
