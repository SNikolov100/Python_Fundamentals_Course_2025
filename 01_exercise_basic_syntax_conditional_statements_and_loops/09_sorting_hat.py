while True:
    name_student = input()
    if name_student == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name_student == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(name_student) < 5:
        print(f"{name_student} goes to Gryffindor.")
    elif len(name_student) == 5:
        print(f"{name_student} goes to Slytherin.")
    elif len(name_student) == 6:
        print(f"{name_student} goes to Ravenclaw.")
    else:
        print(f"{name_student} goes to Hufflepuff.")
