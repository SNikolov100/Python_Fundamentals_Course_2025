def palindrome_words(is_palindrome: list) -> list:
    """list containing all the found palindromes in the sequence"""
    for data in is_palindrome:
        return [data for data in is_palindrome if data == data[::-1]]


is_palindrome_words = input().split()
compare_word = input()

result = palindrome_words(is_palindrome_words)
repetition = result.count(compare_word)
print(result)
print(f"Found palindrome {repetition} times")