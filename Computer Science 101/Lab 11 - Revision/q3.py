import math

def calculate_cars_needed(number_of_people, number_of_seats):
    seats_required = math.ceil(number_of_people / number_of_seats)
    plural = ""
    if seats_required > 1:
        plural = "s"
    print(f"{seats_required} car{plural} needed for {number_of_people} people.")