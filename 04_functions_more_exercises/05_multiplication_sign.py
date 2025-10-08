def multiplication_sign(sequence:list ) -> str:
    """Determinate negative, positive, or zero without use multiplication"""
    if 0 in sequence:
        return "zero"
    sequence_negative = [data for data in sequence if data < 0]
    return "negative" if len(sequence_negative) % 2 != 0 else "positive"


sequence_of_integer = [int(input()) for _ in range(3)]

result = multiplication_sign(sequence_of_integer)
print(result)