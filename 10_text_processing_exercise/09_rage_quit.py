entered_text = input()
new_characters = ""
temp_char = ""
multiplication = ""

for index in range(len(entered_text)):
    if entered_text[index].isdigit():
        multiplication += entered_text[index]
        if (index == len(entered_text) - 1) or not (entered_text[index + 1].isdigit()):
            new_characters += temp_char * int(multiplication)
            temp_char = ""
            multiplication = ""
    else:
        temp_char += entered_text[index].upper()

unique_symbol = len(set(new_characters))
print(f"Unique symbols used: {unique_symbol}")
print(new_characters)

