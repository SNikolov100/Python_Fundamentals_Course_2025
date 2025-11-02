students = int(input())
students_book = {}

for _ in range(students):
    name = input()
    grade = float(input())
    if name not in students_book:
        students_book[name] = []
    students_book[name].append(grade)

for name, grades in students_book.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

