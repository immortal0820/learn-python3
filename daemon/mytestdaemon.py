#!/usr/bin/env python3
#coding: utf-8
#Filename: mytestdaemon.py

import os, sys, daemon, time

class MyTestDaemon(daemon.MyDaemon):
	def __init__(self, save_path, stdin = os.devnull, stdout = os.devnull, stderr = os.devnull, verbose = 1):
		daemon.MyDaemon.__init__(self, save_path, stdin, stdout, stderr, verbose)
		self.name = 'Mytest'

	def run(self):
		with open('/root/mytest_daemon.log', 'a+') as fp:
			while True:
				line = time.ctime() + '\n'
				fp.write(line)
				fp.flush()
				time.sleep(1)

if __name__ == '__main__':
	help_msg = 'Usage: python {0} <start|stop|status|restart>'.format(sys.argv[0])
	if len(sys.argv) != 2:
		print(help_msg)
		sys.exit(1)
	
	pid_fn = '/tmp/mytest_daemon.pid'
	log_fn = '/tmp/mytest_daemon.log'
	err_fn = '/tmp/mytest_daemon.err.log'

	mydaemon = MyTestDaemon(pid_fn, stderr = err_fn)
	if sys.argv[1] == 'start':
		mydaemon.start()
	elif sys.argv[1] == 'stop':
		mydaemon.stop()
	elif sys.argv[1] == 'restart':
		mydaemon.restart()
	elif sys.argv[1] == 'status':
		alive = mydaemon.is_running()
		if alive:
			print('proccess [{0}] is running ......'.format(mydaemon.get_pid()))
		else:
			print('damon process [{0}] stopped'.format(mydaemon.name))
	else:
		print('invalid argument!')
		print(help_msg)

