#!/bin/python3

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Generate a list of numbers under 1000 and test each one for divisibility. Add those divisible by 3 or 5 to a running sum

total = 0
for num in range(1000):
    if num % 3 == 0 and num % 5 != 0:
        total += num
    if num % 5 == 0:
        total += num
    else:
        continue
print( total )
