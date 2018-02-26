from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
identity = new_matrix()
ident(identity)
#add_point(matrix, 2, 3, 4)
print "New matrix:"
print_matrix(matrix)
print "Add 2 points:"
add_point(matrix, 10, 10, 3)
add_point(matrix, 400, 10, 5)
print_matrix(matrix)
print "Multiplying matrix by identity"
matrix_mult(matrix, identity)
print_matrix(matrix)
draw_lines( matrix, screen, color )
display(screen)
