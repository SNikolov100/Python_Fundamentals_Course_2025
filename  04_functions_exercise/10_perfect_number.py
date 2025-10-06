def is_perfect_number(number: int) -> bool:
    sum_number = 0
    for data in range(1, number):
        if number % data == 0:
            sum_number += data

    return sum_number == number


entered_number = int(input())

if is_perfect_number(entered_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")