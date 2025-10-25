def count_dots_function(dots_dashes: list, current_rows: int, current_columns: int) -> int:
    current_count = 0
    count_list = []
    for row in range(current_rows):
        for column in range(current_columns):
            count = 0
            if dots_dashes[row][column] == ".":
                if column - 1 in range(current_columns):
                    if dots_dashes[row][column - 1] == ".":
                        count += 1
                        dots_dashes[row][column] = "-"
                if column + 1 in range(current_columns):
                    if dots_dashes[row][column + 1] == ".":
                        count += 1
                        dots_dashes[row][column] = "-"
                if row - 1 in range(current_rows):
                    if dots_dashes[row - 1][column] == ".":
                        count += 1
                        dots_dashes[row][column] = "-"
                if row + 1 in range(current_rows):
                    if dots_dashes[row + 1][column] == ".":
                        count += 1
                        dots_dashes[row][column] = "-"
            if count != 0:
                current_count += count
            else:
                count_list.append(current_count)
                current_count = 0
    print(count_list)
    counter = max(count_list)
    return counter


rows = int(input())
input_dots_dashes = []
pack_of_dots_dashes = []
columns = 0

for _ in range(rows):
    input_dots_dashes.append(input())

for data in input_dots_dashes:
    pack_of_dots_dashes.append(data.split())
columns = len(input_dots_dashes[0].split())
max_dots = count_dots_function(pack_of_dots_dashes, rows, columns)
print(max_dots)


