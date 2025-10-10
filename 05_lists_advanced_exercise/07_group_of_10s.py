sequence_of_numbers = list(map(int, input().split(", ")))
list_of_groups = []
group = 0
remaining = sequence_of_numbers.copy()

while sequence_of_numbers:
    group += 10
    list_of_groups = [number for number in sequence_of_numbers if number <= group]
    sequence_of_numbers = [number for number in sequence_of_numbers if number > group]
    print(f"Group of {group}'s: {list_of_groups}")
