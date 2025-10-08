entered_names = input().split(", ")

sorted_names_list = sorted(entered_names, key=lambda x: (-len(x), x))

print(sorted_names_list)
