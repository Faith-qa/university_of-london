#!/usr/bin/env python3

'''
Implement the non fruitful function swap_columnd(M,i, j)
that modifies the given Matrix m, by swappint the ith and jth columns
'''

def swap_columns(M, i, j):
    for row in M:
        temp = row[i]
        row[i] = row[j]
        row[j] = temp

M = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
swap_columns(M, 0, 1)
print(M)

#nb the function modifies elements in the list but does 
# not create a new list