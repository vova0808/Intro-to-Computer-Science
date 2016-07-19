# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)


def is_identity_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    elif len(matrix) <= 1:
        return False

    for lst in matrix:
        for number in lst:
            if number > 1 or number < 0:
                return False
        if lst.count(1) > 1:
            return False
        
    i = 0
    j = 0
    while i < len(matrix):
        if matrix[i][j] != 1:
            return False
        i += 1
        j += 1
    return True    
                
                           
    
