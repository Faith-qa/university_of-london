#!/usr/bin/env python3

'''
implement a function

number_of_above_average(A)

that takes a matrix of integers A and returns a number 

of positions(i, j) where an element at this position in A

is greater than the average of all elements in A. As usual position
(i,j) denotes the ith row and jth column in the matrix

'''

def number_of_above_average(A):
    stSum = 0
    stCount = 0
    stPosition = 0

    for row in A:
        for col in row:
            stSum += col
            stCount += 1
    ave = stSum / stCount

    for row in A:
        for col in row:
            if col > ave:
                stPosition += 1
    
    return stPosition

print(number_of_above_average([[1,1], [2,4]]))