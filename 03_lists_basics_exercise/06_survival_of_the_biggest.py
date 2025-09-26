enter_strings = input()
count_remove = int(input())

enter_strings_list = enter_strings.split()
int_list = [int(data) for data in enter_strings_list]
temp_list = [int(data) for data in enter_strings_list]
temp_list.sort(reverse=True)
temp_list = temp_list[-count_remove:]

for data in temp_list:
    if data in int_list:
        int_list.remove(data)

print(", ".join(map(str, int_list)))


