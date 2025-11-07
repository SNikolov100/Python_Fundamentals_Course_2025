text = input()
strength = 0
new_text = ""
for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    else:
        new_text += text[index]
    if text[index] == ">" and index <= len(text):
        strength += int(text[index + 1])

print(new_text)
