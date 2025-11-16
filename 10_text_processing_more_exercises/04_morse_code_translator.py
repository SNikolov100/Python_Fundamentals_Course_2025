# text = "A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- K -.- L .-.. M -- N -. O --- P .--. Q --.- " \
#        "R .-. S ... T - U ..- V ...- W .-- X -..- Y -.-- Z --.."
# morse_code = {}
# entered_char = input().split(" | ")
# result = ""
#
# morse = text.split()
# for index in range(0, len(morse)-1, 2):
#     key, value = morse[index+1], morse[index]
#     morse_code[key] = value
#
# for word in entered_char:
#     strings = word.split()
#     for string in strings:
#         result += morse_code[string]
#     result += " "
#
# print(result)

text = "A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- K -.- L .-.. M -- N -. O --- P .--. Q --.- " \
       "R .-. S ... T - U ..- V ...- W .-- X -..- Y -.-- Z --.."
entered_char = input().split(" | ")
result = ""
morse = text.split()
letters = [morse[index] for index in range(len(morse)) if index % 2 == 0]
codes = [morse[index] for index in range(len(morse)) if index % 2 != 0]
morse_code = dict(zip(codes, letters))
for codes in entered_char:
    code = codes.split()
    for string in code:
        result += morse_code[string]
    result += " "

print(result)

