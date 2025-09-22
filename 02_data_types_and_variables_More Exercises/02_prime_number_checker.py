number_check = int(input())

prime_flag = True

for index in range(2, number_check):
    if number_check % index == 0:
        prime_flag = False

print(prime_flag)