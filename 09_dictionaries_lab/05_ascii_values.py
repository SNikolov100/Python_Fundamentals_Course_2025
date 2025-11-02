list_of_characters = input().split(", ")


# list_to_ascii = [ord(string) for string in list_of_characters]
#
# print(dict(zip(list_of_characters, list_to_ascii)))


# ascii_dictionary = {character: ord(character) for character in list_of_characters}
# print(ascii_dictionary)


ascii_dictionary = {}
for char in list_of_characters:
    ascii_dictionary[char] = ord(char)
print(ascii_dictionary)
