#!/usr/bin/env python
# Filename: pickling.py

import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'banan']

fp = open(shoplistfile, 'wb')	# 二进制写模式打开
pickle.dump(shoplist, fp)
fp.close()

del shoplist

fp = open(shoplistfile, 'rb')	# 二进制读模式打开
recovery = pickle.load(fp)
fp.close

print(recovery)
