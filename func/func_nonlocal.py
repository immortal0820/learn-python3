#!/usr/bin/env python3

def func_outer():
	x = 4
	print('x is', x)

	def func_iner():
		nonlocal x
		x = 10
		
	func_iner()
	print('change x to', x)

func_outer()
