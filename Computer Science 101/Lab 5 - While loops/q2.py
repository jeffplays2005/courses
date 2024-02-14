integer = int(input("Enter an integer number: "));
acc = "not acceptable";
if(integer % 2 == 0 and 0 < integer <= 100):
    acc = "acceptable";
print(f"{integer} is {acc}.")
