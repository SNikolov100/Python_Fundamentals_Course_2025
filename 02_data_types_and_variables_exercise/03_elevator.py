from math import ceil

all_people = int(input())
capacity_elevator = int(input())

result = ceil(all_people / capacity_elevator)
print(result)