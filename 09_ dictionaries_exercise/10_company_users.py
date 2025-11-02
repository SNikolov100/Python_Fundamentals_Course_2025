company_register = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    company_name = command[0]
    employee_id = command[1]
    if company_name not in company_register:
        company_register[company_name] = []
    if employee_id in company_register[company_name]:
        continue
    company_register[company_name].append(employee_id)

for company_name, employee_id in company_register.items():
    print(f"{company_name}")
    print(*[f"-- {employee_id}" for employee_id in employee_id], sep="\n")
