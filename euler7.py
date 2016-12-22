#!/bin/python3

"""
"""

from math import sqrt

def isPrime(num):
    if num == 1:
        return False
    elif num < 4:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    else:
        limit = int(sqrt(num) + 1)
        factor = 5
        while factor <= limit:
            if num % factor == 0:
                return False
            if num % (factor + 2) == 0:
                return False
            factor+=6
        return True
count = 1
test = 1
while True:
    test += 2
    if isPrime(test):
        count+=1
        if count == 10001:
            print(test)
            break

