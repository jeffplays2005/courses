import operator
def postfix(structure):
    numbers = []
    # operators = { "*": 2, "/": 2, "+": 1, "-": 1 }
    operators = { "*": operator.mul, "/": operator.truediv, "+": operator.add, "-": operator.sub }
    # operators = [ '*','/','+','-' ]
    individual_structure = structure.split(' ')
    for i in individual_structure:
        if i in operators.keys():
            # extract last 2
            a = numbers.pop(-2)
            b = numbers.pop(-1)
            numbers.append(operators[i](a,b))
        else:
            numbers.append(int(i))
    return numbers[0]
print(postfix('5 6 3 2 + * -'))