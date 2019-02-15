from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_point( matrix, 0, 1)
add_point( matrix, 1, 2)
add_edge( matrix, 1, 0, 0, 2, 1, 0)
print_matrix( matrix )

print( "Identity matrix of previous matrix:" )
ident( matrix )
print_matrix( matrix )


#draw_lines( matrix, screen, color )
#display(screen)
