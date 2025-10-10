previous_version = input().split(".")
temp_number = int("".join(previous_version))
temp_number += 1
next_version = list(str(temp_number))
print(".".join(next_version))