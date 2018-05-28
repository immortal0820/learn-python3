#!/usr/bin/env python3

ab = {
		'Swaroop' : 'swaroop@swaroopch.com',
		'Larry' : 'larry@wall.org',
		'Infore' : 'inforeyun@infocre.cn',
		'Spamer' : 'spamer@gmail.com'
	 }

print("Swaroop's address is", ab['Swaroop'])

print('Delete a key-value')
del ab['Spamer']
print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {0} at {1}'.format(name, address))

print('Add a key-value')
ab['Guido'] = 'guido@qq.com'
if 'Guido' in ab:   # or ab.has_key('Guido')
	print("\nGuido's address is", ab['Guido'])

ab['Larry'] = 'larry@mail.com'
print('All key and value is', ab)
