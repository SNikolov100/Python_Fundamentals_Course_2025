students = {}
temp_list = []
course = ""
while True:
    information_of_course = input().split(":")
    if len(information_of_course) == 1:
        course = information_of_course[0]
        break
    name, id_person, course = information_of_course[0], information_of_course[1], information_of_course[2]
    if " " in course:
        course = course.replace(" ", "_")
    if course not in students:
        students[course] = []
    students[course].append(name)
    students[course].append(id_person)

for index in range(0, len(students[course]), 2):
    print(f"{students[course][index]} - {students[course][index  + 1]}")



