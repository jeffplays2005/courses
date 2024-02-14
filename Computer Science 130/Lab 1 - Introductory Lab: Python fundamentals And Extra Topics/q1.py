import math
radius = float(input("Enter a radius: "));
height = float(input("Enter a height: "));
print(f"Volume of cone is {math.ceil(1/3 * 3.141592 * radius ** 2 * height)} cubic cm.");

# 1 line
print(f"Volume of cone is {int(-(-((1/3 * 3.141592 * float(input('Enter a radius: ')) ** 2 * float(input('Enter a height: '))))//1))} cubic cm.");
