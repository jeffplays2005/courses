import math;

n1 = float(input("Enter the first number: "));
n2 = float(input("Enter the second number: "));
n3 = float(input("Enter the third number: "));

total = n1 + n2 + n3;

n4 = float(input(f"Enter {n1} + {n2} + {n3} = "));
if(math.isclose(n4, total, rel_tol = 0.0, abs_tol=0.001)):
    print("Correct");
else:
    print("Incorrect")