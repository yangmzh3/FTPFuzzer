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
SLEEP_TIME = 0.1


def login(hostname, port, username, password):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(SOCKET_TIME_OUT)
		s.connect((hostname, port))
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Connect error!")
		s.close()
		return
	
	try:
		s.send("USER" + " " + username + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		s.send("PASS" + " " + password + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		return s
	except:
		print("[-] Login failed!")
		s.close()
		return


def CDUP(hostname, port, username, password, seed, amount):
	s = login(hostname, port, username, password)
	
	#make sure the socket is created.
	if not isinstance(s, socket.socket):
		return
	
	commands = ["CDUP\r\n"]
	try:
		s.send(commands[0])
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Network error!")
		s.close()
		return
		
	if response[0 : 3] == "250":
		print("[+] CDUP is available.")
		time.sleep(SLEEP_TIME * 10)

		for command in commands:
			print("[*] Generating mutated data...")

			bit_flip_cmd = mutate.bit_flip("CDUP", command, seed, amount)
			buffer_overflow_cmd = mutate.buffer_overflow("CDUP", command, seed, amount)
			format_string_cmd = mutate.format_string("CDUP", command, seed, amount)
		
			print("[*] Start fuzzing.Seed value is %d." %seed)
			time.sleep(SLEEP_TIME * 10)
		
			fuzz(s, hostname, "bit_flip", bit_flip_cmd)
			fuzz(s, hostname, "buffer_overflow", buffer_overflow_cmd)
			fuzz(s, hostname, "format_string", format_string_cmd)

		s.close()
	
	else:
		print("CDUP is unavailable.")
		time.sleep(SLEEP_TIME * 10)

		s.close()
		return


def CWD(hostname, port, username, password, seed, amount):
	s = login(hostname, port, username, password)
	
	#make sure the socket is created.
	if not isinstance(s, socket.socket):
		return
	
	commands = ["CWD /\r\n", "CWD ..\r\n"]
	try:
		s.send(commands[0])
		response = s.recv(SOCKET_RECEIVE_LENGTH)
	except:
		print("[-] Network error!")
		s.close()
		return
		
	if response[0 : 3] == "250":
		print("[+] CWD is available.")
		time.sleep(SLEEP_TIME * 10)

		for command in commands:
			print("[*] Generating mutated data...")

			bit_flip_cmd = mutate.bit_flip("CWD", command, seed, amount)
			buffer_overflow_cmd = mutate.buffer_overflow("CWD", command, seed, amount)
			format_string_cmd = mutate.format_string("CWD", command, seed, amount)
			mutate_space_cmd = mutate.mutate_space("CWD", command)
		
			print("[*] Start fuzzing.Seed value is %d." %seed)
			time.sleep(SLEEP_TIME * 10)
		
			fuzz(s, hostname, "bit_flip", bit_flip_cmd)
			fuzz(s, hostname, "buffer_overflow", buffer_overflow_cmd)
			fuzz(s, hostname, "format_string", format_string_cmd)
			fuzz(s, hostname, "mutate_space", mutate_space_cmd)

		s.close()

	else:
		print("CWD is unavailable.")
		time.sleep(SLEEP_TIME * 10)

		s.close()
		return


def fuzz(s, hostname, mode, commands):
	count = 0
	for command in commands:
		try:
			print("[*] [Case %d] Mutate method: %s..." %(count, mode))
			
			if (command[len(command) - 2 : len(command)] != "\r\n"):
				s.send(command + "\r\n")
			else:
				s.send(command)
			
			response = s.recv(SOCKET_RECEIVE_LENGTH)
			time.sleep(SLEEP_TIME)
			count += 1
		except socket.timeout:
			#if no response is received in SOCKET_TIME_OUT,
			#we consider that the host has crashed.
			print("[-] Host has crashed!")
			
			#catch current mutated socket
			now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
			filename = "crashes/" + hostname + "_" + mode + "_" + now + ".txt"
			file = open(filename, "w")
			file.write(command)
			file.close()
			
			time.sleep(SLEEP_TIME)
			count += 1
			continue
		except socket.error:
			print("[-] Network error!")
			s.close()
			return