factor = int(input())
count = int(input())

data_list = []

for index in range(1, count + 1):
    data_list.append(factor * index)

print(data_list)