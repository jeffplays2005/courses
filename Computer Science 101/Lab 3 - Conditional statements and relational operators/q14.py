n = float(input("Enter the numerator: "));
d = float(input("Enter the denominator: "));
r = "Undefined";
if(d != 0):
    r = round(n/d,2);
print(f"Result: {r}");
