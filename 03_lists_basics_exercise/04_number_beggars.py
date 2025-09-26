enter_data = input()
beggars = int(input())

enter_data_list = enter_data.split(", ")
profit = 0
profit_list = []

for start in range(0,beggars):
    profit = 0
    for index in range(start, len(enter_data_list), beggars):
        profit += int(enter_data_list[index])
    profit_list.append(profit)

print(profit_list)




