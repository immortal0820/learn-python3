#!/usr/bin/env python3

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Swaroop'

#Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

#Slicing on list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item test is', shoplist[:3])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

#Slicing on string
print('character 1 to 3 is', name[1:3])
print('character 2 to end is', name[2:])
print('character 1 to -1 is', name[1:-1])
print('character -1 is', name[:-1])
print('character start to end is', name[:])
