fact = int(input("Enter a factor: "));
maximum = int(input("Enter a maximum: "));

i = 1;
while(i <= maximum):
    if(i % fact == 0):
        print(i);
        i+=1;
    else:
        i+=1;
