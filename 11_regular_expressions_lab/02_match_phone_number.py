import re
phone_number_sequence = input()
pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"

result = re.findall(pattern, phone_number_sequence)
print(", ".join(result))


