key = list(map(int, input().split()))
massage = list(input())
sum_of_number = 0
result_massage = []

for number in key:
    sum_of_number = sum(int(digit) for digit in str(number))
    index = sum_of_number % len(massage)
    result_massage.append(massage[index])
    del massage[index]
print("".join(result_massage))



