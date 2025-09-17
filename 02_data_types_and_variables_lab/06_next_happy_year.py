new_year = int(input())
new_year_str = ""

while True:
    new_year += 1
    new_year_str = str(new_year)
    if len(set(new_year_str)) == len(new_year_str):
        print(new_year)
        break
