course_dictionary = {}

while True:
    command = input()
    if command == "end":
        break
    course_info = command.split(" : ")
    course_name = course_info[0]
    student_name = course_info[1]
    if course_name not in course_dictionary:
        course_dictionary[course_name] = []
    if student_name in course_dictionary[course_name]:
        continue
    course_dictionary[course_name].append(student_name)

for course_name, registered_students in course_dictionary.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name} ")
