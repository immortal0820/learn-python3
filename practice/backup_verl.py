#!/usr/bin/env python3
# Filename: backup_verl.py

import os, time

source = ['/root/testpython/practice/']
target_dir = '/root/Desktop'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print(target)

zip_command = "zip -qr {0} {1}".format(target, ' ' .join(source))

print(zip_command)
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup failed')
