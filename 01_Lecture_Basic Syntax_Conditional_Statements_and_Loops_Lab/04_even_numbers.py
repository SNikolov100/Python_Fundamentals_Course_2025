numbers = int(input())

for index in range(numbers):
    int_number = int(input())
    if int_number % 2 != 0:
        print(f"{int_number} is odd!")
        break
else: print("All numbers are even.")
