#/usr/bin/env python
# -*- coding: UTF-8 -*-


#######################################
# Filename : FTPFuzzer.py
# Auther   : yangmzh3
# Date     : 2018-05-23
# Email    : yangmzh3@mail2.sysu.edu.cn
#######################################


import argparse
import sys


#import command.py
import command


SEED = 65535
AMOUNT = 100


def main():
	parser = argparse.ArgumentParser(
		description = "A FTP fuzzer using neural fuzzing tech.")
	
	parser.add_argument("--hostname",
		required = True, help = "hostname of FTP server")
	
	parser.add_argument("--port",
		type = int, default = 21, help = "port of FTP server")
	
	parser.add_argument("--username",
		required = True, help = "required username")
	
	parser.add_argument("--password",
		required = True, help = "required password")

	parser.add_argument("--seed",
		type = int, default = SEED, help = "random seed")

	parser.add_argument("--amount",
		type = int, default = AMOUNT, help = "amount of mutation")
	
	args = parser.parse_args()

	command.CDUP(args.hostname, args.port, args.username, args.password, args.seed, args.amount)
	sys.exit()


if __name__ == "__main__":
	main()