size_of_party = int(input())
days = int(input())
profit = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        size_of_party -= 2
    if day % 15 == 0:
        size_of_party += 5
    profit += 50 - (2 * size_of_party)
    if day % 3 == 0:
        profit -= 3 * size_of_party
    if day % 5 == 0:
        profit += 20 * size_of_party
        if day % 3 == 0:
            profit -= 2 * size_of_party

print(f"{size_of_party} companions received {profit // size_of_party} coins each.")
