miner_dictionary = {}
counter = 0
while True:
    command = input()
    counter += 1
    if command == "stop":
        break
    if counter % 2 != 0:
        resource = command
        if command not in miner_dictionary:
            miner_dictionary[resource] = 0
    else:
        quantity = int(command)
        miner_dictionary[resource] += quantity

for resource, quantity in miner_dictionary.items():
    print(f"{resource} -> {quantity}")
