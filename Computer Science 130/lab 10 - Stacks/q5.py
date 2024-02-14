def postfix_to_infix(expression):
    operands = []
    # operators to capture
    # bracketting to organise sections of an equation
    operators = [ "*", "/", "+", "-" ]
    for i in list(expression):
        if i != " ":
            if i in operators:
                a = operands.pop(-2)
                b = operands.pop(-1)
                operands.append(f'({a}{i}{b})')
            else:
                # step 1, if operand then append to operands
                operands.append(i)
    return "".join(operands)
# no comments
def postfix_to_infix(expression):
    operands = []
    operators = [ "*", "/", "+", "-" ]
    for i in list(expression):
        if i != " ":
            if i in operators:
                a = operands.pop(-2)
                b = operands.pop(-1)
                operands.append(f'({a}{i}{b})')
            else:
                operands.append(i)
    return "".join(operands)
# example
print(postfix_to_infix("23*5+"))
# ((2*3)+5)
#
print(postfix_to_infix('7 9 3 * - 4 +'))
