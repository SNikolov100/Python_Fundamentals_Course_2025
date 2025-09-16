count_coffee = 0

while True:
    command = input()
    if command == "END":
        break

    if command.lower() in ["coding", "dog", "cat", "movie"]:
        count_coffee += 1
        if command.isupper():
            count_coffee += 1
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)
