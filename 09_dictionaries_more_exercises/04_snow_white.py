group_of_dwarf = {}

while True:
    command = input().split(" <:> ")
    if command[0] == "Once upon a time":
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])
    if dwarf_hat_color not in group_of_dwarf:
        group_of_dwarf[dwarf_hat_color] = {}
    if dwarf_name not in group_of_dwarf[dwarf_hat_color]:
        group_of_dwarf[dwarf_hat_color][dwarf_name] = 0
    if dwarf_physics < group_of_dwarf[dwarf_hat_color][dwarf_name]:
        continue
    group_of_dwarf[dwarf_hat_color][dwarf_name] = dwarf_physics

sorted_dwarfs = sorted(
    ((color, name, physics) for color, dwarfs in group_of_dwarf.items() for name, physics in dwarfs.items()),
    key=lambda x: (-x[2], -len(group_of_dwarf[x[0]]))
)
for data in sorted_dwarfs:
    print(f"({data[0]}) {data[1]} <-> {data[2]}")
