#!/usr/bin/env python3

def total(initial=5, *numbers, vegetables):  #vegetables 为关键参数, initial参数不是默认参数，在调用时不指定时，改参数无效
	count = initial
	for number in numbers:
		count += number
	count += vegetables
	return count

print (total(1, 2, 3, vegetables = 50))    #指定关键参数的值，不指定会报错，miss 1 argument, 没有指定initial, return 56
print (total(10, 1, 2, 3, vegetables = 50))    #指定关键参数的值，不指定会报错，miss 1 argument，指定了initial，return 66
