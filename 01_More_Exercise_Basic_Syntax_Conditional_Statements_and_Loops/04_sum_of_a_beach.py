enter_string = input()
enter_string = enter_string.lower()
words = ["sand", "water", "fish", "sun"]
count_words = {}

for word in words:
    count_words[word] = enter_string.count(word)

total_repeat_words = sum(count_words.values())
print(total_repeat_words)
