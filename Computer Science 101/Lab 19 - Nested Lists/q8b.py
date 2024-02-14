"""
Two matrices can be added, if they have the same dimensions.
In other words, both matrices have the same number of rows and the same number of columns.
For example, given matrix A which has m rows and n columns:
[a_11 a_12 ... a_1n]
[a_21 a_22 ... a_2n]
[...  ...  ... ... ]
[a_m1 a_m2 ... a_mn]
and matrix B which has m rows and n columns
[b_11 b_12 ... b_1n]
[b_21 b_22 ... b_2n]
[...  ...  ... ... ]
[b_m1 b_m2 ... b_mn]
Then the sum of matrices A and B, matrix C, also has m rows and n columns.
Each entry in matrix C is the sum of the corresponding entries in matrices A and B.
[a_11+b_11 a_12+b_12 ... a_1n+b_1n]
[a_21+b_21 a_22+b_22 ... a_2n+b_2n]
[...  ...  ... ... ]
[a_m1+b_m1 a_m2+b_m2 ... a_mn+b_mn]
Complete the matrix_addition() function that takes two nested lists, representing 2 matrices, as parameters. If the 2 parameter matrices can be added, i.e., matrixl and matrix2 have the same dimensions, the function returns a new nested list representing the sum of these matrices. Otherwise, the function prints
"Incorrect Dimensions!" and returns -1. Some examples of the function being called are shown below.
"""
# Observations
# The question is wanting to add to matrixes together
# A common pattern can be seen where in each nested list of m1 and m2(m = matrix) and that for
# each row and each column of m1, there is a corresponding row and column in m2 of equal length.
# The objective is to find the corresponding rows and add each element together.
# E.g.
# Let there be 2 matrixes, m1 = [ [1,2,3] ] and m2 = [ [4,5,6] ]
# As the precondition of same number of rows and columns is met(both have 1 row and 3 columns)
# We can proceed.
# As the question states, it would be [ [1+4, 2+5, 3+6] ]
# A nested for loop can be created to add each of the elements of the lists
# The indexes we are adding together are the same, e.g. row1 of m1 and m2 and index 0 of m1/m2
# is 1 and 4, we add them together and add to a new list.
# Therefore, we can make an outer for loop to iterate through the nested lists
# E.g. m1= [ [1,2], [3,4] ], m2 = [[5,6], [6,7]]
# Iterating through the outer loops of m1 and m2 results:
# [1,2] and [3,4] for m1
# [5,6] and [6,7] for m2
# We can create a new list at this point to store our output.
# E.g. m3 = []
# As we only need to iterate through one matrix(assuming that theres the same number of
# columns and rows)
# We can
# for i in len(m1)
# And have the nested lists from both lists as we can use m1[i] and m2[i]
# The inner for loop would loop through each element in m1[i] and m2[i].
# E.g.
# for n in len(m1[i]):
# We can get the indivdual elements at specific nth positions
# E.g. for m1[i] and m2[i], we can use m1[i][n] and m2[i][n]
## E.g. let i = 0
## m1[i] = [1,2]
## m2[i] = [5,6]
### E.g. let n = 0
### We get m1[i][n] = 1
### We get m2[i][n] = 5
### 1+5=6
### Create a temporary list thats in the first for loop, append 6 to the list
### Suppose that the inner for loop completes and then append that temporary list to m3
def matrix_addition(matrix1, matrix2):
    # e.g. m1= [ [1,2], [3,4] ], m2 = [[5,6], [6,7]]
    # Begin by checking the number of rows
    # 2=2 based on example
    if len(matrix1) != len(matrix2):
        print("Incorrect Dimensions!")
        return -1
    # create a matrix 3 output list
    matrix3 = []
    # iterate through the length of matrix1
    for row in range(len(matrix1)):
        # e.g. row = 0,1
        # create a temporary list
        new_list = []
        # m1 and m2
        # In the example, let row = 0
            ## e.g. m1 = [1,2]
            ## e.g. m2 = [5,6]
        matrix1_row = matrix1[row]
        matrix2_row = matrix2[row]
        # check the number of columns
            # in the example, [1,2] and [5,6] both have 2 columns
        if len(matrix1_row) != len(matrix2[row]):
            print("Incorrect Dimensions!")
            return -1
        # inner for loop to iterate through each element of the nested lists
        for column in range(len(matrix1_row)):
                # in this example, let column be 0
                # m1 column would be 1
                # m2 column would be 5
            matrix1_column = matrix1_row[column]
            matrix2_column = matrix2_row[column]
                # total of 1+5 = 6
            matrix3_column = (matrix1_column + matrix2_column)
                # add to the temporary list created earlier
            new_list.append(matrix3_column)
        # all the columns have been added together, can proceed with adding the temporary
        # list to the matrix 3 output list
        matrix3.append(new_list)
    # return
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
