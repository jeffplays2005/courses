"""
Complete the print_number_triangle() function which takes an integer parameter - number_of_rows. 
The function prints a right-angled triangle consisting of consecutive numbers, starting with 1 
in the top left corner of the triangle. The number of rows in the triangle to be printed is 
specified by the parameter.

For example with the following function call:
`print_number triangle(5)`
would produce the output:
01
02 03
04 05 06
07 08 09 10
11 12 13 14 15
"""
# Prelogic/interpretations
# 
# The question is asking to create a function that creates a triangle of numbers
# From the example given, numbers should be 2 digits long(with a 0 at the front 
# when one digit long)
# A common pattern that is visible by analysing the testing cases is that in each n'th row
# there are also n numbers
# 1 | 01 |
# 2 | 02 | 03 |
# 3 | 04 | 05 | 06 |
# 4 | 07 | 08 | 09 | 10 |
# 5 | 11 | 12 | 13 | 14 | 15 |

# As the rows and columns progress, the number also increases. This can be seen as a counter. 
# As each row and column is passed through, the counter should be incremented by 1.
# And if the length of the counter is less than 1, add a 0 to the front of it. 


def print_number_triangle(number_of_rows):
    counter = 1
    rowc = 1
    while rowc <= number_of_rows:
        print_me = []
        for i in range(rowc):
            aaa = str(counter) if len(str(counter)) != 1 else f"0{counter}"
            print_me.append(aaa)
            counter+=1
        print(" ".join(print_me))
        rowc+=1
print_number_triangle(5)
