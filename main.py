from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix2 = new_matrix()
matrix3 = new_matrix()
#for drawing
matrixd = new_matrix()

print( "Matrix 1" )
print_matrix( matrix )
print( "Matrix 2" )
print_matrix( matrix2 )
print( "Matrix 3" )
print_matrix( matrix3 )

print( "Adding points to matrix 1" )
add_point( matrix, 0, 1)
add_point( matrix, 1, 2)
add_edge( matrix, 1, 0, 0, 2, 1, 0)
add_point( matrix, 0, 1)
print_matrix( matrix )

print( "Identity matrix of second matrix" )
ident( matrix2 )
print_matrix( matrix2 )

print( "Adding points to matrix 3" )
add_point( matrix3, 0, 1)
add_point( matrix3, 1, 2)
add_edge( matrix3, 1, 0, 0, 2, 1, 0)
print_matrix( matrix3 )

print( "Multiply third matrix with first matrix" )
matrix_mult( matrix3, matrix)
print_matrix( matrix )

print( "Multiply second matrix (identity) with previous matrix" )
matrix_mult( matrix2, matrix3)
print_matrix( matrix )

i = -250
while i < 500:
    add_edge( matrixd, 0, 0 + i, 0, 250, 250 + i, 0 )
    add_edge( matrixd, 0, 0 + i, 0, 500, 0 + i, 0 )
    add_edge( matrixd, 250, 250 + i, 0, 500, 0 + i, 0 )
    draw_lines( matrixd, screen, color )
    i += 50

print_matrix( matrixd )

display(screen)
