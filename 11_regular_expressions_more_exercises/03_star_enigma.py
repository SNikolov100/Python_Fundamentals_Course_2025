import re

number_of_messages = int(input())
pattern_to_decrypt = r"[star]"
attack_planet = []
destroy_planet = []

for index in range(number_of_messages):
    decrypt_message = ""
    message = input()
    encrypt_message = re.findall(pattern_to_decrypt, message, re.IGNORECASE)
    length = len(encrypt_message)
    for character in message:
        ascii_number = ord(character) - length
        new_char = chr(ascii_number)
        decrypt_message += new_char
    pattern_info_decrypt = r"@([A-Za-z\s]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!([AD])![^@\-!:>]*->([0-9]+)"
    info_decrypt = re.findall(pattern_info_decrypt, decrypt_message)
    if not info_decrypt:
        continue
    planet_name, population, attack_type, solder_count = \
        info_decrypt[0][0], info_decrypt[0][1], info_decrypt[0][2], info_decrypt[0][3]
    if attack_type == "A":
        attack_planet.append(planet_name)
    elif attack_type == "D":
        destroy_planet.append(planet_name)

attack_planet = sorted(attack_planet)
destroy_planet = sorted(destroy_planet)
print(f"Attacked planets: {len(attack_planet)}")
for planet in attack_planet:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroy_planet)}")
for planet in destroy_planet:
    print(f"-> {planet}")




