first_employer = int(input())
second_employer = int(input())
third_employer = int(input())
students = int(input())
count_time = 1

total_students_per_hour = first_employer + second_employer + third_employer
if students == 0:
    count_time = 0

while students > 0:
    if students - total_students_per_hour > 0:
        count_time += 1
        if count_time % 4 == 0:
            continue
        students -= total_students_per_hour
    else:
        students -= total_students_per_hour


print(f"Time needed: {count_time}h.")
