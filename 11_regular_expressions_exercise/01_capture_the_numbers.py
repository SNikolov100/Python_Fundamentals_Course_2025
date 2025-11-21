import re

pattern = r"\d+"

while True:
    command = input()
    if not command:
        break
    numbers = re.findall(pattern, command)
    if numbers:
        print(" ".join(numbers), end=" ")
