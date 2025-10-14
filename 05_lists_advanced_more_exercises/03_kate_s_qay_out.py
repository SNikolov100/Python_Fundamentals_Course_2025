def deep_search(maze: list, start: list, memory: list, visited: list):
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited.append((start[0], start[1]))

    for index_row in range(4):
        row_deep = direction[index_row][0] + start[0]
        col_deep = direction[index_row][1] + start[1]

        if 0 <= row_deep < len(maze) and 0 <= col_deep < len(maze[0]):

            if maze[row_deep][col_deep] != "#" and (row_deep, col_deep) not in visited:
                memory.insert(0, [row_deep, col_deep, start[2] + 1])

    return memory, visited


rows_in_maze = int(input())
start_point = []
max_columns = 0
legend_maze = ""
maze_list = []
memory_points = []
visited_out = []
exit_list = []
max_steps = []
column_maze = 0

for row in range(rows_in_maze):
    legend_maze = input()
    max_columns = len(legend_maze)
    maze_list.append(legend_maze)

    if "k" in legend_maze:
        column_kate = legend_maze.index("k")
        start_point.append(row)
        start_point.append(column_kate)
        start_point.append(0)
column_maze = len(legend_maze)

if start_point[0] == 0\
            or start_point[1] == 0 \
            or start_point[0] == rows_in_maze - 1\
            or start_point[1] == column_maze - 1:
    exit_list.append([start_point[0], start_point[1], 0])
    max_steps.append(0)
while True:
    memory_points, visited_out = \
        deep_search(maze_list, start_point, memory_points, visited_out)

    if not memory_points:
        break
    start_point[0], start_point[1], start_point[2] = memory_points[0][0], memory_points[0][1], memory_points[0][2]

    if memory_points[0][0] == 0\
            or memory_points[0][1] == 0 \
            or memory_points[0][0] == rows_in_maze - 1\
            or memory_points[0][1] == column_maze:

        exit_list.append(memory_points[0])
        max_steps.append(memory_points[0][2])
    del memory_points[0]

if not exit_list:
    print(f"Kate cannot get out")

else:
    print(f"Kate got out in {max(max_steps) + 1} moves")

