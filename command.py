#/usr/bin/env python
# -*- coding: UTF-8 -*-


#######################################
# Filename : command.py
# Auther   : yangmzh3
# Date     : 2018-06-04
# Email    : yangmzh3@mail2.sysu.edu.cn
#######################################


import socket
import time
import sys


#import mutate.py
import mutate


SOCKET_TIME_OUT = 3
SOCKET_RECEIVE_LENGTH = 1024
SLEEP_TIME = 0.0


def login(hostname, port, username, password):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(SOCKET_TIME_OUT)
		s.connect((hostname, port))
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Connect error!")
		return
	
	try:
		s.send("USER" + " " + username + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)

		s.send("PASS" + " " + password + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		
		return s
	
	except:
		print("[-] Login failed!")
		return


def CDUP(hostname, port, username, password, seed, amount):
	s = login(hostname, port, username, password)
	standard_cmd = "CDUP\r\n"
	try:
		s.send(standard_cmd)
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		return
		
	if response[0] == "2":
		print("[+] CDUP is available.\n")
		time.sleep(1.0)

		print("[*] Generating mutate data...")
		##############################
		mutate.buffer_overflow(standard_cmd, seed, amount)
		mutate_cmd = mutate.bit_flip(standard_cmd, seed, amount)
		
		print("[*] Start fuzzing.Current seed value is %d." %seed)
		time.sleep(1.0)
		
		count = 0
		for cmd in mutate_cmd:
			try:
				print("[*] [Case %d] Mutate method: flip bit..." %count)
				s.send(cmd + "\r\n")
				response = s.recv(SOCKET_RECEIVE_LENGTH)
				time.sleep(SLEEP_TIME)
				count += 1
			except socket.timeout:
				#if no response is received in SOCKET_TIME_OUT,
				#we consider that the host has crashed.
				print("[-] Host has crashed!")
	else:
		print("CDUP is unavailable.")


def CWD(hostname, port, username, password, seed, amount):
	try:
		s = login(hostname, port, username, password)
		standard_cmd = "CWD /\r\n"
		s.send(standard_cmd)
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Network error!")