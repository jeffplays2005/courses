"""
Define a function names create_2d_list(word) which takes a string as a parameter and returns
a nested list. For example if the parement word is "cat", then the function would return the
following nested list:
[['c'], ['c', 'a'], ['c', 'a', 't'] ]
Note: You can assume that the paremeter word is not empty
"""
# Prelogic/Notes of observation
# As the given testing case, create_2d_list("cat") produces the list of lists, there is a
# pattern that can be seen.
# Each list, for example denoted by their number in the list position, e.g.
# Indexes:
#   0         1             2
# [['c'], ['c', 'a'], ['c', 'a', 't'] ]
# number of characters
#   1         2             3
# The number of characters simply just correspond to the number of characters that
# is extracted as a substring, e.g. the 0th index(1 character) is only the first character of
# "cat".
# A simple way to complete this is by using a nested for loop, iterating the length of the word
# E.g. "cat" is of length 3, so the indexes given would be 0, 1, 2
# And then simply adding 1 to that and iterating through the indexes(1,2,3)(this is because
# of 0,1,2 all adding 1)
# Therefore, your iteration would be of the following:
# 0,1,2 indexes(corresponding to the position of the output list)
# And the iterating through the index+1 would be: 1,2,3
# Which is the number of characters you want in the list

# We have the indexes and number of characters, which leaves one more thing...the characters
# that we want in the output.
# If we take another look at the output, we notice that:
# Indexes:
#   0         1             2
# [['c'], ['c', 'a'], ['c', 'a', 't'] ]
# number of characters
#   1         2             3
# Character indexes in "cat"
#  0       0, 1       0,1,2

# There is a pattern here where the character indexes in "cat" is something that is iterable
# through the range of number of characters.
# E.g. in ['c', 'a', 't'], there are 3 characters and by iterating through, we get: 0,1,2.

def create_2d_list(word):
    counter = 1;
    two_d_array = []
    while counter < len(word)+1:
        sublist = []
        for pos,i in enumerate(word):
            if pos <= (counter-1):
                sublist.append(i)
        two_d_array.append(sublist)
        counter+=1
    return two_d_array
        
print(create_2d_list('hello'))
