def password_validator_len(pass_string: str) -> str:
    if 6 <= len(pass_string) <= 10:
        return "Password is valid"
    print("Password must be between 6 and 10 characters")


def password_validator_alpha_number(pass_string: str) -> str:
    if pass_string.isalnum():
        return "Password is valid"
    print("Password must consist only of letters and digits")


def password_validator_two_digits(pass_string: str) -> str:
    count_digit = 0
    data = ""
    for data in pass_string:
        count_digit += 1 if data.isdigit() else 0
    if count_digit >= 2:
        return "Password is valid"
    print("Password must have at least 2 digits")


entered_password = input()

result_len = password_validator_len(entered_password)
result_al_num = password_validator_alpha_number(entered_password)
result_two_dig = password_validator_two_digits(entered_password)

if result_len == result_al_num == result_two_dig:
    print(result_len)
