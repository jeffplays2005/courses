import math
print("A quadratic equation has the form: ax^2 + bx + c");
a = int(input("Enter the value for a: "));
b = int(input("Enter the value for b: "));
c = int(input("Enter the value for c: "));

delta = (b**2) - 4*a*c;

if(delta > 0):
    root1 = (-b - math.sqrt(delta)) / (2 * a);
    root2 = (-b + math.sqrt(delta)) / (2 * a);
    print(f"There are two roots: {round(root1, 2)} and {round(root2, 2)}")
elif(delta == 0):
    root = -b / (2 * a);
    print(f"There is a single root: {round(root, 2)}")
else:
    print("There is no root in the space of real numbers.")
