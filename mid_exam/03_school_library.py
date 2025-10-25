def add_book(books: list, commands: list) -> list:
    name_book = commands[1]
    if name_book in books:
        return books
    if len(books) > 0:
        books.insert(0, name_book)
    else:
        books.append(name_book)
    return books


def take_book(books: list, commands: list) -> list:
    name_book = commands[1]
    if name_book in books:
        books.remove(name_book)
    return books


def swap_book(books: list, commands: list) -> list:
    book_first = commands[1]
    book_second = commands[2]
    if book_first in books and book_second in books:
        index_first_book = books.index(book_first)
        index_second_book = books.index(book_second)
        books[index_first_book], books[index_second_book] = books[index_second_book], books[index_first_book]
    return books


def insert_book(books: list, commands: list) -> list:
    name_book = commands[1]
    if name_book in books:
        return books
    books.append(name_book)
    return books


def check_book(books: list, commands: list) -> list:
    index = int(commands[1])
    if index in range(len(books)):
        print(books[index])
    return books


collection_of_books = input().split("&")
command_line = []
while True:
    input_command = input()
    if input_command == "Done":
        break
    command_line = input_command.split(" | ")
    command = command_line[0]
    if command == "Add Book":
        if len(command_line) > 1:
            collection_of_books = add_book(collection_of_books, command_line)
    elif command == "Take Book":
        if len(command_line) > 1:
            collection_of_books = take_book(collection_of_books, command_line)
    elif command == "Swap Books":
        if len(command_line) > 1 and command_line[2]:
            collection_of_books = swap_book(collection_of_books, command_line)
    elif command == "Insert Book":
        if len(command_line) > 1:
            collection_of_books = insert_book(collection_of_books, command_line)
    elif command == "Check Book":
        if len(command_line) > 1 and command_line[1].isdigit():
            if int(command_line[1]) >= 0:
                collection_of_books = check_book(collection_of_books, command_line)

print(", ".join(collection_of_books))

