import math

sin = float(input("Enter the value of sin(π/2): ")) # 1
cos = float(input("Enter the value of cos(π): ")) # -1
sin_1 = float(input("Enter the value of sin(π/6): "))# 0.5

print(f"First answer is {'correct' if math.isclose(1, sin, abs_tol = 0.001) else 'incorrect'}.")
print(f"Second answer is {'correct' if math.isclose(-1, cos, abs_tol = 0.001) else 'incorrect'}.")
print(f"Third answer is {'correct' if math.isclose(0.5, sin_1, abs_tol = 0.001) else 'incorrect'}.")

# 
s = float(input('Enter the value of sin(π/2): '))
c = float(input('Enter the value of cos(π): '))
si = float(input('Enter the value of sin(π/6): '))

import math
sin = (math.sin(math.pi/2))
cos = (math.cos(math.pi))
sin2 = (math.sin(math.pi/6))

if math.isclose(s, sin, abs_tol = 0.001):
    print('First answer is correct.')
else:
    print('First answer is incorrect.')

if math.isclose(c, cos, abs_tol = 0.001):
    print('Second answer is correct.')
else:
    print('Second answer is incorrect.')

if math.isclose(si, sin2, abs_tol = 0.001):
    print('Third answer is correct.')
else:
    print('Third answer is incorrect.')