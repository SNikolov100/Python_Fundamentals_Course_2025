import re
words = []
mirror_words = []
text_string = input()
pattern = r"([@#])([a-z]{3,})\1\1([a-z]{3,})\1"

pattern_words = re.finditer(pattern, text_string, re.IGNORECASE)
for data in pattern_words:
    words.append(data.group(2))
    words.append(data.group(3))

for index in range(len(words) - 1):
    first_word = words[index]
    second_word = words[index + 1]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word + " <=> " + second_word)

if not words:
    print(f"No word pairs found!")
else:
    print(f"{int(len(words) / 2)} word pairs found!")
if not mirror_words:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))



