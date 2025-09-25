number_of_word = int(input())
key_word = input()
words = []
filtered_word = []

for index in range(number_of_word):
    words.append(input())

for word in words:
    if key_word in word:
        filtered_word.append(word)
print(words)
print(filtered_word)


