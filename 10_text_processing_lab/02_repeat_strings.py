sequence_of_strings = input().split()
new_string = ""
for string in sequence_of_strings:
    new_string += string * len(string)
print(new_string)
