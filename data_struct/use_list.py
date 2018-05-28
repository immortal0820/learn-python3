#!/usr/bin/env python

#this is my shop list
shoplist = ['apples', 'mango', 'carrot', 'banan']

print('I have', len(shoplist), 'items to purcase')
print('this items are:', end=' ')

for item in shoplist:
	print(item, end=' ')

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shop list is now', shoplist)

print('I will sort shoplist')
shoplist.sort()
print('Sorted shop list is now', shoplist)

print('I will insert one')
shoplist.insert(3, 'per')
print('Insert shop list is now', shoplist)

print('the first item i will buy is', shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shop list is now', shoplist)
