from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
#ident(matrix)
add_point(matrix, 2, 3, 4)
print_matrix(matrix)


draw_lines( matrix, screen, color )
display(screen)
