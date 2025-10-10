some_text = input().split()
even_word_in_some_text = [text for text in some_text if len(text) % 2 == 0]

print("\n".join(even_word_in_some_text))
