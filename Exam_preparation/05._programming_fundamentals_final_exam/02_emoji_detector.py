import re

cool_emoji = []
entered_text = input()
pattern_emojis = r"(\*\*|::)([A-Z][a-z]{2,})\1"
pattern_digits = r"\d"
cool_threshold_sum = 1
extract_digits = re.findall(pattern_digits, entered_text)
count_cool = 0
for digit in extract_digits:
    cool_threshold_sum = int(digit) * cool_threshold_sum

extract_emojis = re.finditer(pattern_emojis, entered_text)

for emojis in extract_emojis:
    sum_ascii_emojis = 0
    emojis_text = emojis.group(2)
    count_cool += 1
    for char in emojis_text:
        sum_ascii_emojis += ord(char)
    if sum_ascii_emojis > cool_threshold_sum:
        temp_cool_emoji = emojis.group(0)
        cool_emoji.append(temp_cool_emoji)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{count_cool} emojis found in the text. The cool ones are:")

for item in cool_emoji:
    print(item)
