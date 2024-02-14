import math

def calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length):
    strips_per_role = math.floor(wallpaper_roll_length / room_height)
    perimeter = (room_width * 2) + (room_length * 2)
    whole_strips = math.ceil(perimeter / wallpaper_roll_width)
    total_roles = math.ceil(whole_strips / strips_per_role)
    
    return total_roles
    
def display_menu():
    print("""************************
1. Wallpaper Calculation
0. Exit
************************""")

def main():
    while True:
        display_menu()
        selection = input("Enter selection: ")
        if selection == "0":
            print("See you next time!")
            break
        wallpaper_roll_width = float(input("Enter the wallpaper roll width: "))
        wallpaper_roll_length = float(input("Enter the wallpaper roll length: "))
        room_length = float(input("Enter the length of the room: "))
        room_width = float(input("Enter the width of the room: "))
        room_height = float(input("Enter the height of the room: "))
        
        f = calculate(room_width, room_length, room_height, wallpaper_roll_width, wallpaper_roll_length)
        print(f"The total number of wallpaper rolls needed for this room is {f}")
    
main()