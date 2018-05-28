#!/usr/bin/env python3
#Filename: list_and_tuple.py

def powersum(power, divid, *args):
	total = 0
	for i in args:
		total += pow(i, power, divid)	# pow(x, y, z) x**y % z

	return total

print(powersum(2, 2, 3, 4))


