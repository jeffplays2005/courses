def get_polygonal_numbers(sides, terms):
    polygonal_numbers = []
    for n in range(1, terms + 1):
        polygon_number = (((sides - 2) * n ** 2) - (sides - 4) * n) / 2
        polygonal_numbers.append(int(polygon_number))
    return polygonal_numbers
print(f"First 5 triangular numbers are: {get_polygonal_numbers(3, 5)}")