#!/bin/python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
number = int(input("Find the largest prime factor of: "))
test = number
prime = 2
prime_roots = []
while prime < number**0.5:
    while test % prime == 0:
        prime_roots.append(prime)
        test /= prime
        print(test, prime)
    prime += 1
print("done")
