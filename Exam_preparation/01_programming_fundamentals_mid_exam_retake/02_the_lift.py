def input_wagons(wagons_list: list, people: int):
    max_capacity = 4

    for index in range(len(wagons_list)):
        free_space = max_capacity - wagons_list[index]
        wagons_list[index] += min(free_space, people)
        people -= min(free_space, people)
    return wagons_list, people


initial_people = int(input())
wagons = list(map(int, input().split()))

full_wagons, initial_people = input_wagons(wagons, initial_people)

if initial_people == 0 and len(set(full_wagons)) == 1 and full_wagons[0] == 4:
    print(*full_wagons)

elif initial_people == 0:
    print(f"The lift has empty spots!")
    print(*full_wagons)

elif initial_people > 0:
    print(f"There isn't enough space! {initial_people} people in a queue!")
    print(*full_wagons)


