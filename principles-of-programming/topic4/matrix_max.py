#!/usr/bin/env python3

'''
implemen a function matrix_max-index(m) that
returns a tuple(i, j) where i is the row number and j is the
column number of the maximal element of the matrix M
'''

def matrix_max_index(M):
    colMax = 0
    rowMax = 0
    nRows = len(M)

    for i in range(nRows):
        for j in range(0, len(M[i])):
            if M[i][j] > M[rowMax][colMax]:
                colMax = j
                rowMax = i
    return (rowMax, colMax)

M = [[0,4,2,4], [2,3,5,5],[5,1,2,5]]

print(matrix_max_index(M))