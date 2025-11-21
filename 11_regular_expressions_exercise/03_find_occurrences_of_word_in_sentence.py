import re

entered_sentences = input()
key_word = input()

pattern = fr"\b{key_word}\b"

occurrence_in_sentences = re.findall(pattern, entered_sentences, re.IGNORECASE)

print(len(occurrence_in_sentences))
