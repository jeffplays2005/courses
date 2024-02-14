string = input("Enter the string: ");
letter = input("Enter the letter: ");
if(string.find(letter) == -1):
    print(f"The letter {letter} does not appear in {string}.");
else:
    print(f"The index of the first occurrence of {letter} in {string} is {string.find(letter)}.")
    print(f"The index of the last occurrence of {letter} in {string} is {string.rfind(letter)}.")
