def rectangle_area(width: int, height: int) -> int:
    return width * height


width_enter = int(input())
height_enter = int(input())

result = rectangle_area(width_enter, height_enter)
print(result)
