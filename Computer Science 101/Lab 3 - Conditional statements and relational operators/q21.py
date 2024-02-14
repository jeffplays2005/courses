year = int(input("Enter a year: "));
animals = ["Hare", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger"]
index = (year - 1999) % 12
animal = animals[index];
if(year):
    print(f"{year} is the year of the {animal}.");
elif index:
    print(f"{year} is the year of the {animal}.");    
else:
    print(f"{year} is the year of the {animal}.");