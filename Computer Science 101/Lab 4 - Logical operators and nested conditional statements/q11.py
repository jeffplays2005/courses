age = int(input("Enter the age: "));
enrol = input("Is the patient enrolled? (yes/no): ");

fee = 0;

if(enrol == "yes"):
    # enrolled
    if(age < 13):
        fee = 0;
    elif(age < 18):
        fee = 40;
    elif(age < 45):
        fee = 60;
    elif(age < 65):
        fee = 50;
    else:
        fee = 43;
else:
    # not enrolled
    if(age < 5):
        fee = 30;
    elif(age < 13):
        fee = 40;
    else:
        fee = 70;
        
print(f"Fee: ${fee}")