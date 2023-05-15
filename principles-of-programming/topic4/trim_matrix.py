#!/usr/bin/env python3

'''
Implement a non-fruitful function

trim_matrix(M)
that, given a list M of lists M[0], M[1], . . ., modifies M so that it forms a correct matrix.

The modification should make all of the M[i] of the same length by removing from the end of each M[i] a number of elements n, such that M[i] is longer than the shortest list among M[0], M[1], . . . by n.
'''

def trim_matrix(M):
    shRow = len(M[0])

    
    for row in M:
        if len(row) < shRow:
            shRow = len(row)
    for row in M:
        del row[shRow:]



M = [[1,2,3], [12,13],[21,22,23,24]]

trim_matrix(M)
print(M)
   
         

