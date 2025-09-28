people = input().split()
coefficient = int(input())
result = []
jump = 0

while people:
    jump = (jump + coefficient - 1) % len(people)
    result.append(people[jump])
    del people[jump]

print("[" + ",".join(result) + "]")

