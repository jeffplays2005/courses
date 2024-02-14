import math

def calculate_frustum_volume(height, radius1, radius2):
    volume = ((math.pi * height) / 3) * ((radius1 ** 2) + (radius1 * radius2) + (radius2 ** 2))
    return round(volume, 2)