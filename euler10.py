import sympy

total = 0
for i in sympy.primerange(1, 2000000):
	total += i

print(total)
