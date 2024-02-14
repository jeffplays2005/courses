def matrix_addition(matrix1, matrix2):
    matrix3 = []
    if len(matrix1) != len(matrix2):
        print("Incorrect Dimensions!")
        return -1
    for pos, i in enumerate(matrix1):
        new_list = []
        for pos2, n in enumerate(i):
            identical = matrix2[pos]
            if len(identical) != len(i):
                print("Incorrect Dimensions!")
                return -1
            
            new_list.append((int(n) + int(identical[pos2])))
        matrix3.append(new_list)
    return matrix3
    
matrix1 = [[11, 3], [7, 11]]
matrix2 = [[5, 1], [0, 2]]
result = matrix_addition(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} + {matrix2} = {result}")

matrix1 = [[11, 3], [7, 11]]
matrix2 = [[5, 1], [0, 2], [-1, -7]]
result = matrix_addition(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} + {matrix2} = {result}")
    
matrix1 = [[11, 3], [7, 11]]
matrix2 = [[5, 1], [0, 2,3]]
result = matrix_addition(matrix1, matrix2)
if result != -1:
    print(f"{matrix1} + {matrix2} = {result}")
