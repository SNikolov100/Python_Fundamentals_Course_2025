def data_types(data_1: str, data_2: str) -> str:
    if data_1 == "int":
        return f"{int(data_2) * 2}"
    if data_1 == "real":
        return f"{float(data_2) * 1.5:.2f}"
    if data_1 == "string":
        return f"${data_2}$"


entered_manipulator = input()
entered_data = input()

result = data_types(entered_manipulator, entered_data)
print(result)