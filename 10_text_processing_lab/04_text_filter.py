banned_word = input().split(", ")
text = input()

for banned in banned_word:
    text = text.replace(banned, "*" * len(banned))

print(text)
