def no_vowels(text: str, vowel_str: list) -> list:
    """Deletes letters from entered text"""
    return [data for data in text if data.lower() not in vowel_str]


entered_text = input()
vowel_strings = ['a', 'o', 'u', 'e', 'i']

result = no_vowels(entered_text, vowel_strings)
print("".join(result))
