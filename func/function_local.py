#!/usr/bin/env python3

def fun(x):
	print('x is', x)
	x = 10
	print('change x to', x)
	return x

def main():
	x = 24
	ret = fun(x)
	print('local x is', x)
	print('ret is', ret)

main()
