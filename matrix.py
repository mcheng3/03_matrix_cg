import math


def print_matrix( matrix ):
    for i in range(0,4):
        row = ""
        for each in matrix:
           row += str(each[i]) + " "
        print row
        

def ident( matrix ):
    for i in range(0,4):
        matrix[i] = [0] * 4
        matrix[i][i] = 1
            
        

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
