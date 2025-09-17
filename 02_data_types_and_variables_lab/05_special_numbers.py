boundary = int(input())

for number in range(1, boundary+1):
    is_true = False
    sum_numbers = 0
    for value_number in str(number):
        sum_numbers += int(value_number)

    #if (sum_numbers == 5) or (sum_numbers == 7) or (sum_numbers == 11):
    if sum_numbers in [5, 7, 11]:
        is_true = True

    print(f"{number} -> {is_true}")



