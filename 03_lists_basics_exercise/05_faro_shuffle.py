faro_shuffle = input()
count_faro_shuffle = int(input())

faro_shuffle_list = faro_shuffle.split()
length = len(faro_shuffle_list)
result_desk = []

for _ in range(count_faro_shuffle):
    for index in range(length // 2):
        result_desk.append(faro_shuffle_list[index])
        result_desk.append(faro_shuffle_list[index+(length // 2)])
    faro_shuffle_list = result_desk
    result_desk = []
print(faro_shuffle_list)


