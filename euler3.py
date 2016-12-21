#!/bin/python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

While the int "prime" is less than the square root of our target number, divide a copy of our target number down by it until that number is no longer divisible, then increment "prime".


"""

number = int(input("Find the largest prime factor of: "))
test = number
prime = 2
while prime < number**0.5:
    while test % prime == 0:
        test /= prime
        print(test, prime)
    prime += 1
