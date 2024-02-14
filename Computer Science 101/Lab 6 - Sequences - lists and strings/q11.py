string = input("Enter an expression: ");
i = 0;
toggle = 0;
for char in string:
    if char == '(':
        toggle += 1
    elif char == ')':
        toggle -= 1
        if toggle < 0:
            print("Incorrect.")
            break
if toggle == 0:
    print("Correct.")
elif toggle > 0:
    print("Incorrect.")

# 1 liner
(lambda x, counter : print("Incorrect." if "A" in (c:=[ (counter := counter + 1) if i == "(" else (("A" if ((counter:=counter-1) < 0) else counter) if i == ")" else counter) for i in x ]) else ("Incorrect." if (c[-1] != 0) else "Correct.")) )(input("Enter an expression: "), 0)
