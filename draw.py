from display import *
from matrix import *

#how many things are filled
filled = 0

def draw_lines( matrix, screen, color ):
    fill = 0
    while matrix[3][fill + 1] != 0:
        draw_line( matrix[0][fill], matrix[1][fill], matrix[0][fill + 1],  matrix[1][fill + 1] )
        print("Line from " + str(matrix[0][fill]) + str(matrix[1][fill]) + " to " +
        fill += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0)
    add_point( matrix, x1, y1, z1)
    
    

def add_point( matrix, x, y, z=0 ):
    fill = 0
    while matrix[3][fill] != 0:
        fill += 1
    matrix[0][fill] = x
    matrix[1][fill] = y
    matrix[2][fill] = z
    matrix[3][fill] = 1
    print( "\nAdded Point to the matrix in column " + str( fill ) + ":\n" + str( x ) + "\n" + str( y ) +  "\n" + str( z ) + "\n1\n" )


def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
