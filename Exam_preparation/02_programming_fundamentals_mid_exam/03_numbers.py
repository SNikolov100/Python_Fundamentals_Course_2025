sequence_of_integer = list(map(int, input().split()))

average_value = sum(sequence_of_integer) / len(sequence_of_integer)
new_list = [data for data in sequence_of_integer if data > average_value]
new_list.sort(reverse=True)

new_list = new_list[:5] if len(new_list) > 5 else new_list
if not new_list:
    print("No")
else:
    print(*new_list)
