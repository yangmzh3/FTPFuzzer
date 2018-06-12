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


SOCKET_TIME_OUT = 2
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
	
	#make sure the socket is created.
	if not isinstance(s, socket.socket):
		return
	
	command = "CDUP\r\n"
	try:
		s.send(command)
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Network error!")
		return
		
	if response[0] == "2":
		print("[+] CDUP is available.\n")
		time.sleep(1.0)

		print("[*] Generating mutated data...")

		bit_flip_cmd = mutate.bit_flip("CDUP", command, seed, amount)
		buffer_overflow_cmd = mutate.buffer_overflow("CDUP", command, seed, amount)
		format_string_cmd = mutate.format_string("CDUP", command, seed, amount)
		
		print("[*] Start fuzzing.Current seed value is %d." %seed)
		time.sleep(1.0)
		
		fuzz(s, "bit_flip", bit_flip_cmd, seed, amount)
		fuzz(s, "buffer_overflow", buffer_overflow_cmd, seed, amount)
		fuzz(s, "format_string", format_string_cmd, seed, amount)
	else:
		print("CDUP is unavailable.")
		return


def fuzz(s, mode, commands, seed, amount):
	count = 0
	for command in commands:
		try:
			print("[*] [Case %d] Mutate method: %s..." %(count, mode))
			s.send(command + "\r\n")
			response = s.recv(SOCKET_RECEIVE_LENGTH)
			time.sleep(SLEEP_TIME)
			count += 1
		except socket.timeout:
			#if no response is received in SOCKET_TIME_OUT,
			#we consider that the host has crashed.
			print("[-] Host has crashed!")
			
			#catch current mutated socket
			now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
			filename = "crashes/" + mode + "_" + now + ".txt"
			file = open(filename, "w")
			file.write(command)
			file.close()
			
			time.sleep(SLEEP_TIME)
			count += 1
			continue
		except socket.error:
			print("[-] Network error!")
			return