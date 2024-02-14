sec = input("Please enter the code: ")
temp = sec.split("(")
temp.pop(0)
temp = "(".join(temp).split(")")
temp.pop()
temp = ")".join(temp)

if not temp:
    print("No secret message!")
else: print(f"Secret message: {temp}")
