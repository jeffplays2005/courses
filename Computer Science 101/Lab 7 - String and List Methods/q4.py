string = input("Enter a phrase: ");
split = string.split(" ");
acronym = "";
for part in split:
    acronym += (part[0].upper());
    
print(f"{acronym}")
