string_numbers = int(input())
char_check = [",", ".", "_"]

for index in range(string_numbers):
    string = input()
    # if any(ind_check in string for ind_check in char_check):
    if ("." in string) or ("," in string) or ("_" in string):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
