def corresponding_grade(grade_receive: float) -> str:
    if 2.00 <= grade_receive <= 2.99:
        return "Fail"
    elif 3.00 <= grade_receive <= 3.49:
        return "Poor"
    elif 3.50 <= grade_receive <= 4.49:
        return "Good"
    elif 4.50 <= grade_receive <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_receive <= 6.00:
        return "Excellent"


grade = float(input())
print(corresponding_grade(grade))
