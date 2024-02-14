def infix_to_postfix(expression):
    # output
    operands = []
    # operators to capture
    # bracketting to organise sections of an equation
    operators = { "*": 2, "/": 2, "+": 1, "-": 1 }
    brackets = [ '(', ')' ]
    operators_found = []
    opening = 0
    for i in list(expression):
        if i != " ":
            if i == brackets[0]: # is opening bracket
                # step 2, if is opening bracket, add to operators found
                operators_found.append(i)
                opening += 1
            elif i == brackets[1]: # is closing bracket
                # step 3, right parenthisis, pop!
                # keep going until found opening bracket
                operators_found.append(i) # saved here for future possible use
                operators_found.pop(-1) # print above for steps
                while len(operators_found) > 0 and operators_found[-1] != brackets[0]:
                    operands.append(operators_found.pop(-1))
                operators_found.pop(-1)
                opening -= 1
            elif i in operators.keys(): # is an operator
                if opening == 0:
                    while len(operators_found) > 0 and operators[operators_found[-1]] >= operators[i]:
                        operands.append(operators_found.pop(-1))
                else:
                    operators_found.append(i)
            else:
                # step 1, if is an operand, we add to operands
                operands.append(i)
    while len(operators_found) > 0:
        operands.append(operators_found.pop(-1))
    print(operators_found)
    return " ".join(operands)
# testing case
print(infix_to_postfix("((2 * 3) + 5)"))
print(infix_to_postfix('(8 * ((4 - 3) + 6))'))
# 2 3 * 5 +