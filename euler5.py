#!/bin/python3

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestcomp(num):
    # Return the smallest positive number evenly divisible by 2 - "num"
    # Multiply the largest numbers in range that are not factors of each other, than divide the result by numbers in the range until the smallest multiple is found
    total = 1
    numbers = list(range(1,num+1))
    numbers.reverse()
    for i in numbers:
        if total % i == 0:
            continue
        else:
            total *= i
    smallest_factor = 2
    print(total)
    test = total
    while True:
        print(smallest_factor)
        test = test / smallest_factor; print("test =", test)
        for i in numbers:
            print ("i =", i)
            print ("test % i =", test % i)
            if test % i != 0:
                test *= smallest_factor
                smallest_factor += 1
                break
        if smallest_factor > num:
            return test
       #smallest_factor += 1
        

num = int(input("number: "))
print(smallestcomp(num))
