bakery = input().split()
bakery_dict = {}

for index in range(0, len(bakery), 2):
    food = bakery[index]
    quantities = int(bakery[index + 1])
    bakery_dict[food] = quantities

print(bakery_dict)