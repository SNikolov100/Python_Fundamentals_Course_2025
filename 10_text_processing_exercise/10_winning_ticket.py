def result_function(dictionary: dict, ticket_print: str):
    for symbol, uninterrupted_length in dictionary.items():
        if uninterrupted_length == 10:
            return f'ticket "{ticket_print}" - {uninterrupted_length}{symbol} Jackpot!'
        elif uninterrupted_length >= 6:
            return f'ticket "{ticket_print}" - {uninterrupted_length}{symbol}'


tickets = input().split(",")
tickets = [data.strip() for data in tickets]
winning_symbols = ('@', '#', '$', '^')
mach_symbol = ""
temp_count_first_dict = {}
temp_count_second_dict = {}

for ticket in tickets:
    if not ticket:
        continue
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    first_half, second_half = ticket[:10], ticket[10:]

    for char in first_half:
        if char in winning_symbols:
            if mach_symbol and char == mach_symbol[0]:
                mach_symbol += char
            else:
                mach_symbol = char
            if len(mach_symbol) >= 6:
                key = mach_symbol[0]
                temp_count_first_dict[key] = len(mach_symbol)
        else:
            mach_symbol = ""
    mach_symbol = ""
    for char in second_half:
        if char in winning_symbols:
            if mach_symbol and char == mach_symbol[0]:
                mach_symbol += char
            else:
                mach_symbol = char
            if len(mach_symbol) >= 6:
                key = mach_symbol[0]
                temp_count_second_dict[key] = len(mach_symbol)
        else:
            mach_symbol = ""
    mach_symbol = ""
    is_first_valid = False
    is_second_valid = False
    temp_count_first = 0
    temp_count_second = 0
    for match_symbol, uninterrupted_match_length in temp_count_first_dict.items():
        if uninterrupted_match_length >= 6:
            is_first_valid = True
            temp_count_first = uninterrupted_match_length
    for match_symbol, uninterrupted_match_length in temp_count_second_dict.items():
        if uninterrupted_match_length >= 6:
            is_second_valid = True
            temp_count_second = uninterrupted_match_length

    if is_first_valid and is_second_valid and (temp_count_first_dict.keys() == temp_count_second_dict.keys()):
        if temp_count_first >= temp_count_second:
            print(result_function(temp_count_second_dict, ticket))
        else:
            print(result_function(temp_count_first_dict, ticket))
    else:
        print(f'ticket "{ticket}" - no match')
    temp_count_first_dict.clear()
    temp_count_second_dict.clear()
