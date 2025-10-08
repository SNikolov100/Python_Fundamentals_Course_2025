temp_list = []
entered_notes = []
while True:
    command = input()
    if "End" in command:
        break
    entered_notes.append(command.split("-"))

for index in range(len(entered_notes)):
    temp_list = sorted(entered_notes, key=lambda x: int(x[0]))

only_text = [data[1] for data in temp_list]

print(only_text)




