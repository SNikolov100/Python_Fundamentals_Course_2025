enter_number = input()
new_number = ""
count = len(str(enter_number))

for index in range(count-1, -1, -1):
    new_number += enter_number[index]

print(new_number)