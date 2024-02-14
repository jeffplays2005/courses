import math

def calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length):
    strips_per_role = math.floor(wallpaper_roll_length / room_height)
    perimeter = (room_width * 2) + (room_length * 2)
    whole_strips = math.ceil(perimeter / wallpaper_roll_width)
    total_roles = math.ceil(whole_strips / strips_per_role)
    return total_roles
print(calculate(2, 4, 2.1, 0.53, 10.05))