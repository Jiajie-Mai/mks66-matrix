"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    #variable declaration
    cols = len(matrix)
    rows = len(matrix[0])
    output = ""
    #adds all the values in each sublist into one string and then each new sublist has a new line
    for r in range( rows ):
        for c in range ( cols ):
            output += " " + str(matrix[c][r])
        output += "\n"
    #print entire thing
    print(output)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    #variable declaration
    output = new_matrix()
    cols = len(output)
    rows = len(output)
    #goes through the list, if the row number and column is the same, a one will be added
    '''
        0 1 2 3

    0   1 0 0 0
    1   0 1 0 0
    2   0 0 1 0
    3   0 0 0 1
    '''
    for c in range( cols ):
        for r in range ( rows ):
            if c == r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    matrix = output


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for row in range(len(m2)):
        listCopy = []
        for col in range(4):
            listCopy.append(m2[row][col])
        for col in range(4):
            sub = 0
            for i in range(4):
                sub += listCopy[i] * m1[i][col]
            m2[row][col] = sub

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
