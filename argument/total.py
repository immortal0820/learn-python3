#!/usr/bin/env python3

def total(initial=5, *numbers, **keywords): # *param 表示从那一点后的所有参数被收集到param的列表中，
	count = initial                         # 此例中numbers=(1, 2, 3);
	for number in numbers:					# **param 表示从那一点开始的所有关键字参数收集到param字典中，
		count += number						# 此例中keywords='vegetables':50, 'fruits':100
	for key in keywords:
		count += keywords[key]
	return count

print(total(10, 1, 2, 3, vegetables=50, fruits=100))
