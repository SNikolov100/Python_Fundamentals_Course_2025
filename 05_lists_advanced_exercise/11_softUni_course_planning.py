def add_lesson_title(lesson: list, command: list) -> list:
    title = command[1]
    if title not in lesson:
        lesson.append(title)
    return lesson


def insert_lesson_title(lesson: list, command: list) -> list:
    index_lesson = int(command[2])
    title = command[1]
    index_lesson = min(index_lesson, len(lesson))
    if command[1] not in lesson:
        lesson = lesson[0:index_lesson] + [title] + lesson[index_lesson:len(lesson)]
    return lesson


def remove_lesson_title(lesson: list, command: list) -> list:
    title = (command[1])
    title_exercise = (command[1] + "-Exercise")
    lesson = [data for data in lesson if data != title and data != title_exercise]
    return lesson


def swap_lesson_title(lesson: list, command: list) -> list:
    title_one = command[1]
    title_two = command[2]
    exercise_one = title_one + "-Exercise"
    exercise_two = title_two + "-Exercise"
    if title_one in lesson and title_two in lesson:
        index_one = lesson.index(title_one)
        index_two = lesson.index(title_two)
        lesson[index_one], lesson[index_two] = lesson[index_two], lesson[index_one]

        if exercise_one in lesson:
            lesson.remove(exercise_one)
            new_index_one = lesson.index(title_one)
            lesson.insert(new_index_one + 1, exercise_one)
        if exercise_two in lesson:
            lesson.remove(exercise_two)
            new_index_two = lesson.index(title_two)
            lesson.insert(new_index_two + 1, exercise_two)
    return lesson


def exercise_lesson_title(lesson: list, command: list) -> list:
    title = command[1]
    title_exercise = title + "-Exercise"
    if title in lesson and title_exercise not in lesson:
        title_lesson_index = lesson.index(title)
        lesson.insert(title_lesson_index + 1, title_exercise)
    elif title not in lesson and title_exercise not in lesson:
        lesson.append(title)
        lesson.append(title_exercise)
    return lesson


schedule_of_lesson = input().split(", ")
general_title = []

while True:
    input_command = input()
    if input_command == "course start":
        break
    command_list = input_command.split(":")
    if command_list[0] == "Add":
        schedule_of_lesson = add_lesson_title(schedule_of_lesson, command_list)

    elif command_list[0] == "Insert":
        schedule_of_lesson = insert_lesson_title(schedule_of_lesson, command_list)

    elif command_list[0] == "Remove":
        schedule_of_lesson = remove_lesson_title(schedule_of_lesson, command_list)

    elif command_list[0] == "Swap":
        schedule_of_lesson = swap_lesson_title(schedule_of_lesson, command_list)

    elif command_list[0] == "Exercise":
        schedule_of_lesson = exercise_lesson_title(schedule_of_lesson, command_list)

for index in range(len(schedule_of_lesson)):
    print(f"{index + 1}.{schedule_of_lesson[index]}")
