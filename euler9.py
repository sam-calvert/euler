#!/bin/python
from math import sqrt
squares = []

# create a list of squares to search through 
for i in range(1,1000):
    squares.append(i**2)

# starting from the largest squares, iterate through the list, subtracting other squares to isolate pythagorean triplets
squarelist = squares
squares.reverse()
for i in squares:
    for j in squarelist:
        if j > i:
            continue
        else:
            diff = i - j
            # when we find a pythagorean triplet, test to see if the square roots (a, b, and c) sum to 1000.
            if diff in squares:
                a = sqrt(diff)
                b = sqrt(j)
                c = sqrt(i)
                if a + b + c == 1000:
                    print a, b, c
                    print a * b * c
                    break
                    
                     
            
