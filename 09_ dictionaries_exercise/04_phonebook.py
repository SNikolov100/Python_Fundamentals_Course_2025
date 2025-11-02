phone_book_dictionary = {}
number_of_search_people = 0

while True:
    phone_numbers = input().split("-")
    if len(phone_numbers) == 1:
        number_of_search_people = int(phone_numbers[0])
        break
    name = phone_numbers[0]
    number = phone_numbers[1]
    phone_book_dictionary[name] = number

for _ in range(number_of_search_people):
    name = input()
    if name not in phone_book_dictionary.keys():
        print(f"Contact {name} does not exist.")
    else:
        number = phone_book_dictionary[name]
        print(f"{name} -> {number}")
