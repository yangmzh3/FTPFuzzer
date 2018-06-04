#/usr/bin/env python
# -*- coding: UTF-8 -*-


#######################################
# Filename : command.py
# Auther   : yangmzh3
# Date     : 2018-06-04
# Email    : yangmzh3@mail2.sysu.edu.cn
#######################################


import socket


#import mutate.py
import mutate


SOCKET_TIME_OUT = 2
SOCKET_RECEIVE_LENGTH = 1024


def login(hostname, port, username, password):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(SOCKET_TIME_OUT)
		s.connect((hostname, port))
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response)

		s.send("USER" + " " + username + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response)

		s.send("PASS" + " " + password + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response)

		return s
	
	except:
	#except socket.timeout:
		pass
		#do nothing temporarily


def CDUP(hostname, port, username, password, seed, amount):
	try:
		s = login(hostname, port, username, password)
		standard_cmd = "CDUP\r\n"
		s.send(standard_cmd)
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response)

		if response[0] == "2":
			print("CDUP is available.\r\n")
			
			mutate_cmd = mutate.flip_bit(standard_cmd, seed, amount)
			for cmd in mutate_cmd:
				try:
					print(cmd)
					s.send(cmd)
					response = s.recv(SOCKET_RECEIVE_LENGTH)
					print(response)		
				except socket.timeout:
					#if no response is received in SOCKET_TIME_OUT,
					#we consider that the host has crashed.
					print("Host has crashed!")
		else:
			print("CDUP is unavailable.\r\n")
	except:
		pass
		#do nothing temporarily


def CWD(hostname, port, username, password, seed, amount):
	try:
		s = login(hostname, port, username, password)
		standard_cmd = "CWD /\r\n"
		s.send(standard_cmd)
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response)
	except:
		pass
		#do nothing temporarily