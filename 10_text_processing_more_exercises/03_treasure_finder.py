key_sequence = (input().split())

while True:
    work_string = input()
    counter_key = 0
    result_string = ""
    if work_string == "find":
        break
    for index in range(len(work_string)):
        if counter_key >= len(key_sequence):
            counter_key = 0
        result_string += chr(ord(work_string[index]) - int(key_sequence[counter_key]))
        counter_key += 1
    treasure = result_string.split("&")
    start_point_for_coordinates = result_string.find("<")
    end_point_for_coordinates = result_string.find(">")
    coordinates = result_string[start_point_for_coordinates + 1:end_point_for_coordinates]

    print(f"Found {treasure[1]} at {coordinates}")



