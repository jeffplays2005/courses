text = input("Enter your text: ")
no = []
for char in text:
    if not char.isalpha() and not char.isdigit():
        no.append(char.strip())
print(''.join(no))
