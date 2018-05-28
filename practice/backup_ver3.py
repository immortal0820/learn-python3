#!/usr/bin/env python3
#Filename: backup_ver3.py

import os, time

source = ['/root/testpython/practice', '/root/testpython/module']
target_dir = '/root/Desktop'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter comment--> ')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' \
			+ comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created dir', today)

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
	print('Successfully backup')
else:
	print('Backup FAILED')
