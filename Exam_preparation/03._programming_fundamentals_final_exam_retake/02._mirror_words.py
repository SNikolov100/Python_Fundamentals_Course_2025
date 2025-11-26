import re

list_of_mirror_words = []
list_of_pair_words = []
text_string = input()
pattern = r"([@#])([a-z]{3,})\1{2}([a-z]{3,})\1"

words = re.finditer(pattern, text_string, re.IGNORECASE)

for word in words:
    temp_word = ""
    word_one = word.group(2)
    word_two = word.group(3)
    if word_one != "" and word_two != "":
        for char in word_two[::-1]:
            temp_word += char
        if temp_word == word_one:
            list_of_mirror_words.append([word_one, word_two])
        list_of_pair_words.append([word_one, word_two])

if not list_of_pair_words:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(list_of_pair_words)} word pairs found!")
    if list_of_mirror_words:
        print(f"The mirror words are:")
        result = ', '.join(f"{one} <=> {two}" for one, two in list_of_mirror_words)
        print(result)
    else:
        print("No mirror words!")


