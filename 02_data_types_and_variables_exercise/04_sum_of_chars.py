numbers_of_char = int(input())
total_sum = 0

for index in range(numbers_of_char):
    letter = int(ord(input()))
    total_sum += letter

print(f"The sum equals: {total_sum}")

