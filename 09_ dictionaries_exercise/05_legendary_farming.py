materials_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
is_mission_completed = False
while True:
    materials = input().lower().split()
    for index in range(0, len(materials), 2):
        material = materials[index + 1]
        quantity = int(materials[index])
        if material not in materials_dictionary:
            materials_dictionary[material] = 0
        materials_dictionary[material] += quantity
        if (material == "shards") or (material == "fragments") or (material == "motes"):
            if materials_dictionary[material] >= 250:
                materials_dictionary[material] -= 250
                if material == "shards":
                    print(f"Shadowmourne obtained!")
                elif material == "fragments":
                    print(f"Valanyr obtained!")
                else:
                    print(f"Dragonwrath obtained!")
                is_mission_completed = True
                break
    if is_mission_completed:
        break
if "shards" in materials_dictionary:
    print(f"shards: {materials_dictionary['shards']}")
    del materials_dictionary["shards"]
if "fragments" in materials_dictionary:
    print(f"fragments: {materials_dictionary['fragments']}")
    del materials_dictionary["fragments"]
if "motes" in materials_dictionary:
    print(f"motes: {materials_dictionary['motes']}")
    del materials_dictionary["motes"]

for material, quantity in materials_dictionary.items():
    print(f"{material}: {quantity}")


