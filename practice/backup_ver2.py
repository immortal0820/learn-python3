#!/usr/bin/env python3
# Filname: backup_ver2.py

import os, time

source = ['"/root/testpython/practice"']
target_dir = '/root/Desktop'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created dir', today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
	print("Successfully backup")
else:
	print('Backup FAILED')
