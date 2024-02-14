"""
Two matrices can be multiplied, if the number of columns in the first matrix is equal to
the number of rows in the second matrix.
For example, given matrix A which has m rows and n columns:
[a_11 a_12 ... a_1n]
[a_21 a_22 ... a_2n]
[...  ...  ... ... ]
[a_m1 a_m2 ... a_mn]
and matrix B which has n rows and p columns
[b_11 b_12 ... b_1p]
[b_21 b_22 ... b_2p]
[...  ...  ... ... ]
[b_n1 b_n2 ... b_np]
Then the product of matrices A and B, matrix C, has m rows and p columns:
[c_11 c_12 ... c_1p]
[c_21 c_22 ... c_2p]
[...  ...  ... ... ]
[c_m1 c_m2 ... c_mp]
Each entry in matrix C, C_ij, is obtained by multiplying term-by-term,
the entries of the ith row of A and the jth column of B, and summing these n products.
C =
[a_11 a_12 ... a_1n]
[a_21 a_22 ... a_2n]
[...  ...  ... ... ]
[a_m1 a_m2 ... a_mn]

Complete the matrix_multiplication() function that takes two nested lists, representing
2 matrices, as parameters. If the 2 parameter matrices can be multiplied, i.e., the number
of columns in matrix1 is equal to the number of rows in matrix2, the function returns a new
nested list representing the product of these matrices. Otherwise, the function prints
"Incorrect Dimensions!" and returns -1. Some examples of the function being called are shown below.
"""

def matrix_multiplication(matrix1, matrix2):
    # the number of columns in matrix1 is equal to the number of rows in matrix2
    if(len(matrix1[0]) != len(matrix2)):
        print("Incorrect Dimensions!")
        return -1
    #  matrix1                 matrix2                      output
    # [[11, 3], [7, 11]]     [[8, 0, 1],[0, 3, 5]]       [[88, 9, 26], [56, 33, 62]]
    #
    # [[11, 3],   +           [8, 0, 1], =               [88(11*8 + 3*0), 9(11*0 + 3*3), 26(11*1 + 3*5)]
    # [7, 11]]    +           [0, 3, 5] =                [56, 33, 62]
    
    matrix_list = []
    
    for row_i in matrix1: # m1 rows
        # 0,1      |    2 rows
        row_list = []
        for n in range(len(matrix2[0])): # m2 columns
            # 0,1,2(1,2,3) 3 columns
            # fetch the column from matrix2
            column_i = [] # from matrix2
            # fetch the columns
            # e.g. column 1(index 0) inside of matrix2
            #  matrix1                 matrix2                      output
            # [[11, 3],   +           [->8<-, 0, 1], =               [88, 9, 26]
            # [7, 11]]    +           [->0<-, 3, 5] =                [56, 33, 62]
            for row in matrix2:
                column_i.append(row[n])
            # create a counter(this is the total of everything multiplied together)
            total = 0
            for pos in range(len(row_i)):
                rowII = row_i[pos]
                columnII = column_i[pos]
                total += rowII * columnII
            row_list.append(total)
        matrix_list.append(row_list)
    return matrix_list

matrix1 = [[11, 3], [7, 11]]
matrix2 = [[8, 0, 1],[0, 3, 5]]
result = matrix_multiplication(matrix1, matrix2)
if result != -1:
   print(f"{matrix1} * {matrix2} = {result}")

matrix1 = [[2, 3], [0, -1]]
matrix2 = [[1, 3]]
result = matrix_multiplication(matrix1, matrix2)
if result != -1:
   print(f"{matrix1} * {matrix2} = {result}")
