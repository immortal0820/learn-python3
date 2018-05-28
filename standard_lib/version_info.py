#!/usr/bin/env python3
#Filename: version_info.py

import sys, warnings

if sys.version_info[0] < 3:
	warnings.warn('Need Python 3.0 for this program to run', RuntimeWarning)
else:
	print('Process as normal!')
