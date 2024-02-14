f = round(float(input("Enter the first number: ")),3);
s = round(float(input("Enter the second number: ")),3);
t = float(input(f"Enter {f} * {s} = "));
if((f*s - 0.002) < t < (f*s + 0.002)):
    print("Correct");
else:
    print("Incorrect");
