def multiplication(first:str, second: str, sum_of_multiplication:int) -> int:
    sum_of_multiplication = 0
    for inx in range(len(first)):
        sum_of_multiplication += ord(first[inx]) * ord(second[inx])
    return sum_of_multiplication


first_string, second_string = input().split()
total_sum = 0

if len(first_string) == len(second_string):
    total_sum = multiplication(first_string , second_string, total_sum)

elif len(first_string) > len(second_string):
    total_sum = multiplication(second_string, first_string, total_sum)
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])

elif len(second_string) > len(first_string):
    total_sum = multiplication(first_string, second_string, total_sum)
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])

print(total_sum)
