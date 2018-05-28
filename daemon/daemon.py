#!/usr/bin/env python3
#coding: utf-8
#Filename: daemon.py

import os, sys, time, atexit, signal

class MyDaemon:
	'''
	a generic daemon class.
	usage: subclass the MyDaemon class and override the run() method
	stderr: error log file
	verbose: default 1, print except info in run of start, 1 is start
	pidfile: pid file
	'''
	def __init__(self, pidfile, stdin = os.devnull, stdout = os.devnull, stderr = os.devnull, verbose = 1):
		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr
		self.verbose = verbose
		self.pidfile = pidfile

	def daemonize(self):
		try:
			pid = os.fork()		# 第一次fork，生成子进程，脱离父进程
			if pid > 0:
				sys.exit(0)
		except OSError as e:
			sys.stderr.write('fork #1 failed: {0} ({1})\n'.format(e.errno, e.strerror))
			sys.exit(1)

		os.chdir('/')
		os.setsid()
		os.umask(0)

		try:
			pid = os.fork()		# 第二次fork，禁止进程打开终端
			if pid > 0:
				sys.exit(0)
		except OSError as e:
			sys.stderr.write('fork #2 failed: {0} ({1})\n'.format(e.errno, e.strerrno))
			sys.exit(1)
		
		# 重定向文件描述符
		sys.stdout.flush()
		sys.stderr.flush()

		with open(self.stdin, 'r') as si:
			os.dup2(si.fileno(), sys.stdin.fileno())
		with open(self.stdout, 'a+') as so:
			os.dup2(so.fileno(), sys.stdout.fileno())
		with open(self.stderr, 'a+') as se:
			os.dup2(se.fileno(), sys.stderr.fileno())

		# 注册退出函数，根据文件pid判断是否存在进程
		atexit.register(self.del_pid)
		pid = str(os.getpid())
		with open(self.pidfile, 'w+') as fp:
			fp.write(pid)

	def get_pid(self):
		try:
			with open(self.pidfile, 'r') as pf:
				pid = int(pf.read().strip())
		except IOError:
			pid = None
		except SystemExit:
			pid = None
		return pid

	def del_pid(self):
		if os.path.exists(self.pidfile):
			os.remove(self.pidfile)

	def start(self):
		if self.verbose >= 1:
			print('ready to start......')
		pid = self.get_pid()
		if pid:
			msg = 'pid file {0} already exists, is it already running?\n'.format(self.pidfile)
			sys.stderr.write(msg)
			sys.exit(1)

		# start daemon
		self.daemonize()
		self.run()

	def stop(self):
		if self.verbose >=1:
			print('stopping......')

		pid = self.get_pid()
		if not pid:
			msg = 'pid file {0} does not exist. Not running?\n'.format(self.pidfile)
			sys.stderr.write(msg)
			if os.path.exists(self.pidfile):
				os.remove(self.pidfile)
			return 

		# try to kill the daemon process
		try:
			i = 0
			while 1:
				os.kill(pid, signal.SIGTERM)
				time.sleep(0.1)
				i = i + 1
				if i % 10 == 0:
					os.kill(pid, signal.SIGHUP)

		except OSError as err:
			err = str(err)
			if err.find('No such process') > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
			else:
				sys.exit(1)

			if self.verbose >= 1:
				print('Stopped!')

	def restart(self):
		self.stop()
		self.start()

	def is_running(self):
		pid = self.get_pid()
		return pid and os.path.exists('/proc/{0}'.format(pid))

	def run(self):
		print('base class run()')
