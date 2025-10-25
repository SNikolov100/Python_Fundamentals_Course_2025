from math import ceil

numbers_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = []
attendance_list = []
is_none = True

if total_number_of_lectures == 0 or numbers_of_students == 0:
    max_bonus = 0
    max_attendance_student = 0
    is_none = False
else:
    for student in range(numbers_of_students):
        if total_number_of_lectures == 0:
            max_bonus = 0
            max_attendance_student = 0
            is_none = False
            break
        attendance = int(input())
        bonus = (attendance / total_number_of_lectures) * (5 + additional_bonus)
        total_bonus.append(bonus)
        attendance_list.append(attendance)
if is_none:
    max_bonus = max(total_bonus)
    index_max_bonus = total_bonus.index(max_bonus)
    max_attendance_student = attendance_list[index_max_bonus]

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance_student} lectures.")


