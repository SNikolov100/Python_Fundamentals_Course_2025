days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
gather_plunder = 0

for day in range(1, days_of_plunder + 1):
    gather_plunder += daily_plunder
    gather_plunder += daily_plunder * 0.5 if day % 3 == 0 else 0
    gather_plunder -= gather_plunder * 0.3 if day % 5 == 0 else 0

if gather_plunder >= expected_plunder:
    print(f"Ahoy! {gather_plunder:.2f} plunder gained.")
else:
    percentage_left_plunder = (gather_plunder * 100) / expected_plunder
    print(f"Collected only {percentage_left_plunder:.2f}% of the plunder.")

