def add_urgent(products: list, items:list) -> list:
    item = items[1]
    if item not in products:
        products.insert(0, item)
    return products


def remove_unnecessary(products: list, items: list) -> list:
    item = items[1]
    if item in products:
        products.remove(item)
    return products


def rename_correct(products: list, items: list) -> list:
    old_name = items[1]
    new_name = items[2]
    if old_name in products:
        index_old_name = products.index(old_name)
        products[index_old_name] = new_name
    return products


def remove_and_add_rearrange(products: list, items: list) -> list:
    item = items[1]
    if item in products:
        products.remove(item)
        products.append(item)
    return products


groceries_products = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    if command[0] == "Urgent":
        groceries_products = add_urgent(groceries_products, command)
    elif command[0] == "Unnecessary":
        groceries_products = remove_unnecessary(groceries_products, command)
    elif command[0] == "Correct":
        groceries_products = rename_correct(groceries_products, command)
    elif command[0] == "Rearrange":
        groceries_products = remove_and_add_rearrange(groceries_products, command)

print(", ".join(groceries_products))
