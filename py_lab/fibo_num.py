#!/usr/bin/python

n = int(input("fibonacci number? "))

a = 1
b = 0
for i in range(n):
	a, b = b, a + b
	if (i == n-1):
		print(b)
		break
	print("%d," %b, end="")

print("F%d = %d" %(n,b)) 

