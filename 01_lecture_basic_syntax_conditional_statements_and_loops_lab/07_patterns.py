max_number_patterns = int(input())

for index in range(1, max_number_patterns+1):
    print(index * "*")
for index in range(max_number_patterns-1, 0, -1):
    print(index * "*")