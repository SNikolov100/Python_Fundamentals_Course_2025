enter_char = int(input())
count = 0
symbols_list = []
symbols_temp = []
symbols_const = ["(", ")"]
unbalanced_flag = False

for _ in range(enter_char):
    char = input()
    if (char == "(") or (char == ")"):
        symbols_list.append(char)

count = len(symbols_list)
if count % 2 == 0:
    for index in range(0, count, 2):
        symbols_temp = symbols_list[index:(index + 2)]
        if symbols_const != symbols_temp:
            unbalanced_flag = True
            break
    if unbalanced_flag:
        print("UNBALANCED")
    else:
        print("BALANCED")
else:
    print("UNBALANCED")



