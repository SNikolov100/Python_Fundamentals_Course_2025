number_of_rooms = int(input())

chairs_visitors = [input() for _ in range(number_of_rooms) ]
number_of_room = 0
is_need_chairs = False
total_free_chairs = 0
for data in chairs_visitors:
    number_of_room += 1
    chairs, visitors = data.split()
    needed_chairs_in_room = len(chairs) - int(visitors)
    if needed_chairs_in_room < 0:
        print(f"{abs(needed_chairs_in_room)} more chairs needed in room {number_of_room}")
        is_need_chairs = True

    total_free_chairs += needed_chairs_in_room
if not is_need_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")