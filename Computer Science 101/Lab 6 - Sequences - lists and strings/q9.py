word = input("Enter a word: ");
amt = 0
for i in range(len(word)):
    if word[i].lower() in ["a", "e", "i", "o", "u"]:
        amt += 1;
print(f"{amt} vowels.")
