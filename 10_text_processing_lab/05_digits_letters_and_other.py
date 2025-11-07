text = input()
text_digit = ""
text_letter = ""
text_other = ""

for character in text:
    if character.isdigit():
        text_digit += character
    elif character.isalpha():
        text_letter += character
    else:
        text_other += character

print(text_digit)
print(text_letter)
print(text_other)
