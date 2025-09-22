# first_value = int(input())
# second_value = int(input())
# temp_value = 0
#
# print(f"Before:\na = {first_value}\nb = {second_value}")
# temp_value = first_value
# first_value = second_value
# second_value = temp_value
# print(f"After:\na = {first_value}\nb = {second_value}")

values = [int(input()), int(input())]
print(f"Before:\na = {values[0]}\nb = {values[1]}")
values[0], values[1] = values[1], values[0]
print(f"After:\na = {values[0]}\nb = {values[1]}")
