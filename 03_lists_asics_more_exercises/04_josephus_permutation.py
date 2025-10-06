number_of_people = input().split()
jump_person = int(input()) - 1

executed_list = []
index = jump_person
while number_of_people:
    if index >= len(number_of_people):
        index %= len(number_of_people)
    executed_list.append(number_of_people[index])
    number_of_people.pop(index)
    index += jump_person

print("[" + ",".join(executed_list) + "]")

