#!/bin/python3

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



def is_palindrome(num):
    # test for palindromicity by comparing the last digit to the first. If they are the same, remove them, and repeat.
    test = str(num)
    while len(test) > 1:
        if test[0] == test[-1]:
            test = test[1:-1]
        #    print(test)
        else:
            return False
    return True

def large_pal(digit):
    # return largest palindrome product of two "digit" length numbers
    # starting from highest possible answer, test whether palindrome and decrement if not. For palindromes, test if the product of two "digit" length numbers.
    upper_limit = 10**digit - 1
    lower_limit = 10**(digit - 1)
    for i in range(upper_limit**2, lower_limit**2, -1):
        if is_palindrome(i):
           # print(i)
            for div in range(upper_limit, lower_limit, -1):
                if i % div == 0 and i/div <= upper_limit:
                    return i

print (large_pal(3))
