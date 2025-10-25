def collect_add(journal_func: list, item_func: str) -> list:
    if item_func in journal_func:
        return journal_func
    journal_func.append(item_func)
    return journal_func


def drop_remove(journal_func: list, item_func: str) -> list:
    if item_func in journal_func:
        journal_func.remove(item_func)
    return journal_func


def renew_move(journal_func: list, item_func: str) -> list:
    if item_func in journal_func:
        index_item = journal_func.index(item_func)
        temp_item = journal_func.pop(index_item)
        journal_func.append(temp_item)
    return journal_func


def combine_items_swap(journal_func: list, command_func: str, item_func: str) -> list:
    list_item = item_func.split(":")
    old_item = list_item[0]
    new_item = list_item[1]
    if old_item in journal_func:
        index_old_item = journal_func.index(old_item)
        journal_func.insert(index_old_item + 1, new_item)
    return journal_func


journal = input().split(", ")
take_items = []

while True:
    input_command = input()
    if input_command == "Craft!":
        break
    sequence_command = input_command.split(" - ")
    command = sequence_command[0]
    item = sequence_command[1]
    if command == "Collect":
        journal = collect_add(journal, item)
    elif command == "Drop":
        journal = drop_remove(journal, item)
    elif command == "Combine Items":
        journal = combine_items_swap(journal, command, item)
    elif command == "Renew":
        journal = renew_move(journal, item)

print(", ".join(journal))