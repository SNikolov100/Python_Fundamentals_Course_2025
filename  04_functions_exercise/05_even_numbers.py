def is_even(number: str) -> bool:
    try:
        return int(number) % 2 == 0
    except ValueError:
        return False


sequence_of_numbers = input().split()

result = list(filter(is_even, sequence_of_numbers))
print(f"[" + ", ".join(result) + "]")
