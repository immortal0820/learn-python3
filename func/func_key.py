#!/usr/bin/env python3

def func(a, b = 5, c = 10):
	print('a is ', a, 'and b is', b, 'and c is', c)

func(3, 7)   
func(25, c = 24)	    #c为关键参数
func(c = 50, a = 100)   #c, a为关键参数
