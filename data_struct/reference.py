#!/usr/bin/env python3

print("Simple arguments")
shoplist = ['apple', 'banana', 'mango']
print('Origner shoplist is', shoplist)

mylist = shoplist       # 复制一个列表或者类似的序列或者其他复杂的对象，必须使用切片操作符来取得拷贝
						# 列表的复制语句不创建拷贝
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]	
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
