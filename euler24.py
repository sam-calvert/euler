#!/bin/python3

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

digits = input("digits: ") # assume no commas or formatting

#counting_dict =
#for digit in digits:
#    counting_dict[digit] = 0
#
#for dig in digits:

diglist = []
for digit in digits:
    diglist.append(int(digit))

diglist.sort()
print(diglist)
    
