#/usr/bin/env python
# -*- coding: UTF-8 -*-

#######################################
# Filename : FTPFuzzer.py
# Auther   : yangmzh3
# Date     : 2018-05-23
# Email    : yangmzh3@mail2.sysu.edu.cn
#######################################


import socket
import argparse
import sys


SOCKET_TIME_OUT = 1
SOCKET_RECEIVE_LENGTH = 1024


def ACCT(hostname, port, username, password):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(SOCKET_TIME_OUT)
		s.connect((hostname, port))
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response + "\r\n")

		s.send("USER " + username + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response + "\r\n")

		s.send("PASS " + password + "\r\n")
		response = s.recv(SOCKET_RECEIVE_LENGTH)
		print(response + "\r\n")
	
	except:
		errorMessage = "ERROR!\r\n"###
		print(errorMessage)###


def main():
	parser = argparse.ArgumentParser(
		description = "A FTP fuzzer using neural fuzzing tech.")
	
	parser.add_argument("--hostname",
		required = True, help = "hostname of FTP server")
	
	parser.add_argument("--port",
		required = True, type = int, help = "port of FTP server")
	
	parser.add_argument("--username",
		required = True, help = "required username")
	
	parser.add_argument("--password",
		required = True, help = "required password")
	
	args = parser.parse_args()

	ACCT(args.hostname, args.port, args.username, args.password)
	sys.exit()


if __name__ == "__main__":
	main()