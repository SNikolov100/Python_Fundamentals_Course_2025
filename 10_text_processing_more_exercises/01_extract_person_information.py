numbers_of_lines = int(input())
is_write_name = False
is_write_age = False
name = ""
age = 0

for _ in range(numbers_of_lines):
    entered_string = input()
    start_index = entered_string.find("@") + 1
    end_index = entered_string.find("|")
    name = entered_string[start_index: end_index]

    start_index = entered_string.find("#") + 1
    end_index = entered_string.find("*")
    age = entered_string[start_index: end_index]

    print(f"{name} is {age} years old.")
