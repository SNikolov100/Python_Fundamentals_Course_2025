def loading_bar(number: int) -> tuple[str, str]:
    if number == 100:
        return "100% Complete!", "[%%%%%%%%%%]"
    temp_number = (number // 10)
    bar = f"{temp_number *10}% [" + "%" * temp_number + "." * (10 - temp_number) + "]"
    massage = "Still loading..."
    return bar, massage


entered_number = int(input())

result = loading_bar(entered_number)
print(result[0])
print(result[1])


