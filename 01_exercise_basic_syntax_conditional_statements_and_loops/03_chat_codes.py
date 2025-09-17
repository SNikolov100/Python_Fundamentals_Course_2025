number_messages = int(input())
result_for_print = ""

for _ in range(number_messages):
    enter_number = int(input())
    if enter_number == 88:
        result_for_print = "Hello"
    elif enter_number == 86:
        result_for_print = "How are you?"
    elif enter_number < 88:
        result_for_print = "GREAT!"
    else:
        result_for_print = "Bye."
    print(result_for_print)
