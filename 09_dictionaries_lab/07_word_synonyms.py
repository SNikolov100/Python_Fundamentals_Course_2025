count_of_words = int(input())
dictionary_of_synonyms = {}

for count in range(count_of_words):
    word = input()
    synonym = input()
    if word not in dictionary_of_synonyms:
        dictionary_of_synonyms[word] = []
    dictionary_of_synonyms[word].append(synonym)

for word, synonym in dictionary_of_synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
