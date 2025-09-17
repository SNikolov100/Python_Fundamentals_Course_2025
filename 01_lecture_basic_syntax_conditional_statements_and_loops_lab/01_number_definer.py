number = float(input())
result = ""
result_small_large = ""
if number == 0:
    print("zero")
else:
    if number > 0:
        result = "positive"
    else:
        result = "negative"
    if 0 < abs(number) < 1:
        result_small_large = "small"
    elif abs(number) > 1000000:
        result_small_large = "large"
    if result_small_large == "":
        print(result)
    else:
        print(result_small_large, result)
