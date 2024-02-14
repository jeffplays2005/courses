start = int(input("Enter the start: "));
end = int(input("Enter the end: "));

string = f"{start}";
if(start <= end):
    start = int(start) + 1;
    while(start <= end):
        string = f"{string} {start}";
        start = int(start) + 1;
    print(string);
else:
    print();
