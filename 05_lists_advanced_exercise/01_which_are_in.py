sequence_one = input().split(", ")
sequence_two = input().split()
substring = [data for data in sequence_one if any(data in data_two for data_two in sequence_two)]

print(substring)