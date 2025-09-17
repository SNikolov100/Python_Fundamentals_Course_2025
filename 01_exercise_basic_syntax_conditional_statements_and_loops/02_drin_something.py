person_age = int(input())
result_drink = ""

if person_age <= 14:
    result_drink = "toddy"
elif person_age <= 18:
    result_drink = "coke"
elif person_age <= 21:
    result_drink = "beer"
else:
    result_drink = "whisky"

print(f"drink {result_drink}")