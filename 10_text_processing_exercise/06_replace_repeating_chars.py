text = input()
new_text = text[0]

for index in range(1, len(text)):
    if text[index] != text[index - 1]:
        new_text += text[index]

print(new_text)
