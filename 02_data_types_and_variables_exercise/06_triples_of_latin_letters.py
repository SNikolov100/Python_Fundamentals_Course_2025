number_possibility = int(input())
result = ""

for data1 in range(97, 97 + number_possibility):
    for data2 in range(97, 97 + number_possibility):
        for data3 in range(97, 97 + number_possibility):
            result = chr(data1) + chr(data2) + chr(data3)
            print(result)
