import re
result = []
entered_string = input()
pattern = r"(^|(?<=\s))(-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

match_numbers = re.finditer(pattern, entered_string)

for digit in match_numbers:
    result.append(str(digit.group(0)))

print(" ".join(result))
