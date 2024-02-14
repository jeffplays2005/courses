def prompt():
    x,y = prompt_i();

    print(f"A triangle with base {x} and height {y} has an area of {float(x*y / 2)}")
            
    try_again = input("Calculate another area (y/n)? ");
    if(try_again == "y"):
        prompt();
def prompt_i():
    base = int(input("Enter the base: "));
    height = int(input("Enter the height: "));
    return base,height;
prompt();
