enter_queue = input()

queue_list = enter_queue.split(", ")
queue_list.reverse()
wolf_index = [(index + 1) for index, data in enumerate(queue_list) if data == "wolf"]

if wolf_index[0] == 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {(wolf_index[0] - 1)}! You are about to be eaten by a wolf!")


