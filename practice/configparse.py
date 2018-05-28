#!/usr/bin/env python3
#coding: utf-8
#Filename: configparse.py

import configparser

cf = configparser.ConfigParser()
# 读配置文件
cf.read('mytest.cnf')

# 判断是否有mysqld sections
if cf.has_section('mysqld'):
	print('file have mysqld section')

# 以列表的形式返回所有的sections
s = cf.sections()
print('sections:', s)

# 得到指定sections的所有option
options = cf.options('mysqld')
print('options:', options)

# 得到指定sections的所有键值对
kvs = cf.items('mysql')
print('mysql:', kvs)

# 指定sections、option(key)读取值
str_val = cf.get('mysqld', 'datadir')
print('datadir:', str_val)

# 写配置文件
# 更新指定section，option的值
cf.set('mysqld', 'datadir', '/usr/local/mysql/data')

# 写入指定section增加新的option，value
cf.set('mysql', 'dir', '/root/testpython/practice')

# 增加新的section
cf.add_section('tb_info')
cf.set('tb_info', 'user', '/root/name/mysql')

# 写回配置文件
with open('mytest.cnf', 'w') as fp:
	cf.write(fp)
