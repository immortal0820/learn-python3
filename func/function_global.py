#!/usr/bin/env python3

x = 19

def fun():
	global x  #	声明x为全局变量

	print('x is', x)
	x = 10	  # 改变x的值，也反映到主块中
	print('change x to', x)

fun()
print('local x is', x)	# x 改变
