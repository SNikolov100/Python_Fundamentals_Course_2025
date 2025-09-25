numbers_of_data = int(input())

data_list = []
result = []
for _ in range(numbers_of_data):
    data_list.append(int(input()))

keyword = input()

if keyword == "even":
    result = [data for data in data_list if data % 2 == 0]
elif keyword == "odd":
    result = [data for data in data_list if data % 2 != 0]
elif keyword == "negative":
    result = [data for data in data_list if data < 0]
elif keyword == "positive":
    result = [data for data in data_list if data >= 0]

print(result)


