start_value = ord(input())
end_value = ord(input())
entered_string = input()
total_sum_strings = 0

for string in entered_string:
    if start_value < ord(string) < end_value:
        total_sum_strings += ord(string)

print(total_sum_strings)