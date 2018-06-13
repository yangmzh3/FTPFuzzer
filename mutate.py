#/usr/bin/env python
# -*- coding: UTF-8 -*-


#######################################
# Filename : mutate.py
# Auther   : yangmzh3
# Date     : 2018-06-04
# Email    : yangmzh3@mail2.sysu.edu.cn
#######################################


import random
import math


#import numpy lib
import numpy


def bit_flip(COMMAND, command, seed, amount):
	numpy.random.seed(seed)
	randnum = numpy.random.randint(0, 128, size = amount)
	mutation = command[len(COMMAND) :]
	bit_flip_cmd = []
	
	position = 0
	while amount > 0:
		head = mutation[0 : position]
		tail = mutation[position + 1 : len(mutation)]
		char = chr((ord(mutation[position]) + randnum[amount - 1]) % 128)
		bit_flip_cmd.append(COMMAND + head + char + tail)
		
		position += 1
		position %= len(mutation)
		amount -= 1
	
	return bit_flip_cmd


def buffer_overflow(COMMAND, command, seed, amount):
	length = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
	
	numpy.random.seed(seed)
	randnum = numpy.random.randint(0, 128, size = amount + 4096)
	mutation = command[len(COMMAND) :]
	buffer_overflow_cmd = []
	
	position = 0
	while amount > 0:
		head = mutation[0 : position]
		tail = mutation[position : len(mutation)]
		
		temp = 0
		buff = ""
		while temp < length[amount % len(length) - 1]:
			buff += chr(randnum[amount + temp])
			temp += 1

		buffer_overflow_cmd.append(COMMAND + head + buff + tail)
		
		position += 1
		position %= len(mutation) + 1
		amount -= 1
	
	return buffer_overflow_cmd


def format_string(COMMAND, command, seed, amount):
	length = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

	numpy.random.seed(seed)
	randnum = numpy.random.randint(0, 128, size = amount)
	mutation = command[len(COMMAND) :]
	format_string_cmd = []

	position = 0
	while amount > 0:
		head = mutation[0 : position]
		tail = mutation[position : len(mutation)]

		temp = 0
		string = ""
		while temp < length[amount % len(length) - 1]:
			string += ("%" + chr(randnum[amount - 1]))
			temp += 1

		format_string_cmd.append(COMMAND + head + string + tail)

		position += 1
		position %= len(mutation) + 1
		amount -= 1

	return format_string_cmd


def mutate_space(COMMAND, command, seed, amount):
	pass


def number(COMMAND, command, seed, amount):
	#not sure
	pass


def mutate_parser(COMMAND, command, seed, amount):
	pass


def mutate_end(COMMAND, command, seed, amount):
	pass


def escape_string(COMMAND, command, seed, amount):
	pass