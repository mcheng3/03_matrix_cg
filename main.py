from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
i = new_matrix()
ident(i)
print_matrix(i)
#add_point(matrix, 2, 3, 4)
print "\nNew matrix:"
print_matrix(matrix)

print "\nAdd 2 points:"
add_point(matrix, 10, 10, 3)
add_point(matrix, 400, 10, 5)
print_matrix(matrix)

print "\nMultiplying matrix by identity:"
matrix_mult(i, matrix)
print_matrix(matrix)

print "\nAdd edges (green):"
add_edge(matrix, 400, 10, 5, 250, 250, 10)
add_edge(matrix, 250, 250, 10, 10, 10, 3)
print_matrix(matrix)

draw_lines( matrix, screen, color )

print "\nTranslate matrix up 50 (yellow):"
i[3][1] = 50
#print_matrix(i)
matrix_mult(i, matrix)
print_matrix(matrix)

draw_lines( matrix, screen, [255, 255, 0] )

print "\nScale matrix by 1.2 (white):"
i = new_matrix()
ident(i)
for c in range(4):
	i[c][c] = 1.2
matrix_mult(i, matrix)
print_matrix(matrix)
draw_lines( matrix, screen, [255,255,255] )

print "\nTranslate matrix left 10 and down 15 (cyan):"
i = new_matrix()
ident(i)
i[3][0] = -10
i[3][1] = -15
matrix_mult(i, matrix)
print_matrix(matrix)

draw_lines( matrix, screen, [0,255,255] )
display(screen)
