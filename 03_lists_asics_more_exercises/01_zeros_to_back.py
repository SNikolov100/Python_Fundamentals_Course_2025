entered_data = input().split(", ")
new_list = []
counter = 0
for data in entered_data:
    if data == "0":
        counter += 1
    else:
        new_list.append(data)

for _ in range(0, counter):
    new_list.append("0")

print(list(map(int, new_list)))
