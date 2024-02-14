counter = 0;
total = 0;

def prompt(c, t):
    x = float(input("Enter a number: "));
    if(x <= 0 and c == 0):
        print("Average: undefined");
    elif(x <= 0):
        print(f"Average: {t / c}");
    else:
        c += 1;
        t += x;
        prompt(c, t);
    
prompt(counter, total);
