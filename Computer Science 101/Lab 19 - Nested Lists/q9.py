def matrix_multiplication(matrix1, matrix2):
    if(len(matrix1[0]) != len(matrix2)):
        print("Incorrect Dimensions!")
        return -1
        
    #  matrix1                 matrix2                      output
    # [[11, 3], [7, 11]]     [[8, 0, 1],[0, 3, 5]]       [[88, 9, 26], [56, 33, 62]]
    #
    # [[11, 3],   +           [8, 0, 1], =               [88, 9, 26]
    # [7, 11]]    +           [0, 3, 5] =                [56, 33, 62]
    
    matrix_list = []
    
    for i in range(len(matrix1)): # m1 rows
        row_list = []
        for n in range(len(matrix2[0])): # m2 columns
            row_i = matrix1[i]
            column_i = [k[n] for k in matrix2]
            total = 0
            for pos, num in enumerate(row_i):
                total += num * column_i[pos]
            row_list.append(total)
        matrix_list.append(row_list)
    return matrix_list

# matrix1 = [[11, 3], [7, 11]]
# matrix2 = [[8, 0, 1],[0, 3, 5]]
# result = matrix_multiplication(matrix1, matrix2)
# if result != -1:
#    print(f"{matrix1} * {matrix2} = {result}")
# 
matrix1 = [[2, 3], [0, -1]]
matrix2 = [[1, 3]]
result = matrix_multiplication(matrix1, matrix2)
if result != -1:
   print(f"{matrix1} * {matrix2} = {result}")