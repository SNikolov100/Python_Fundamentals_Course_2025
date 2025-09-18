enter_number = input()

enter_number_list = list(enter_number)

enter_number_list.sort(reverse=True)

print(int("".join(enter_number_list)))



