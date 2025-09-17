# while True:
#     string_word = input()
#     if string_word == "End":
#         break
#     if string_word == "SoftUni":
#         continue
#
#     for index in range(len(string_word)):
#         for _ in range(2):
#             print(string_word[index], end = "")
#     print()


while True:
    result_word = ""
    string_word = input()
    if string_word == "End":
        break
    if string_word == "SoftUni":
        continue

    for index in range(len(string_word)):
        result_word += 2 * string_word[index]
    print(result_word)