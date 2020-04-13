#!/usr/bin/python
import sys

n = int(input("How many numbers will you enter? "))

sum = 0
for i in range(1, n+1):
	temp = int(input())
	sum += temp

avg = sum / n

print("average is %d" % avg)
