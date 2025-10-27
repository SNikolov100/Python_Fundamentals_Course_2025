enter_data = list(map(int, input().split(", ")))

new_list = [data for data in enter_data if data != 0]
new_list += [0 for _ in range(len(enter_data) - len(new_list))]

print(new_list)

