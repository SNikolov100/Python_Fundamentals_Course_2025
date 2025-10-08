entered_employers = list(map(int, input().split()))
improve_happy = int(input())

multiply_happy_employers = [data * improve_happy for data in entered_employers]
total_employers = len(multiply_happy_employers)
average_happy = sum(multiply_happy_employers) / total_employers
happy_employer = list(filter(lambda x: x >= average_happy, multiply_happy_employers))
count_happy_employers = len(happy_employer)


if count_happy_employers < (total_employers / 2):
    result = "are not happy!"
else:
    result = "are happy!"

print(f"Score: {count_happy_employers}/{total_employers}. Employees {result}")


