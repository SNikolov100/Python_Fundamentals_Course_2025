number_snowballs = int(input())

max_value = 0
max_wight = 0
max_time = 0
max_quality = 0

for _ in range(number_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality
    if max_value <= value:
        max_value = value
        max_wight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality


print(f"{max_wight} : {max_time} = {max_value:.0f} ({max_quality})")
