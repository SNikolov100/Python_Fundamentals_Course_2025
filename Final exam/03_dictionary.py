dictionary = {}

words_and_definition = input().split(" | ")
only_words = input().split(" | ")
for words in words_and_definition:
    word, definition = words.split(": ")
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)

command = input()
if command == "Test":
    for test_word in only_words:
        if test_word in dictionary:
            print(f"{test_word}:")
            for definition in dictionary[test_word]:
                print(f" -{definition}")

elif command == "Hand Over":
    print(" ".join(word for word in dictionary))



