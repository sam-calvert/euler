roots = []; product = 1; x = 2; number = input("number?: "); y = number
while product != number:
	while (y % x == 0):
		print "y =", y, "x =", x, "roots =", roots, "product =", product
		roots.append(x)
		y /= x
		#product *= roots[-1]
	x += 1
print roots
