divisor = int(input())
boundary = int(input())
max_number = divisor

if divisor > 0:
    for index in range(boundary, 0, -1):
        if index % divisor == 0:
            max_number = index
            break
print(f"{max_number}")
