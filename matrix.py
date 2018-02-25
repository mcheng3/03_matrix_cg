import math


def print_matrix( matrix ):
    for i in range(len(matrix[0])):
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
    m = [[] for x in range(0,4)]
    m3 = []
    row = 0
    for r1 in range(0,4):
        for c2 in range(0,len(m2[0])):
            sum = 0
            for i in range(0,len(m1[0])):
                prod = m1[i][r1] * m2[c2][i]
                sum += prod
            #print str(sum) + " " + str(r1)
            m[r1].append(sum)
    #print_matrix(m)
    m2[:] = list(m)



def new_matrix(rows = 4, cols = 4):   
    m = []
    i = 0
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( i )
            i += 1
    return m
