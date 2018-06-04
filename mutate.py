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


def calculate_length(seed):
	random.seed(seed)
	random.random()
	length = int(round(random.random() * 256.0))
	if length == 0:
		length += 1
	while 256 % length == 0:
		length += 1
	return length


def flip_bit(standard_cmd, seed, amount):
	#mutate position of cmd
	mutate_position = 0

	#mutate ascii length of loop
	mutate_ascii_length = calculate_length(seed)

	#mutate startup position's ascii value, just assign it the same as length of loop
	mutate_ascii = mutate_ascii_length

	mutate_cmd = []
	
	while amount > 0:
		mutate_position = mutate_position % len(standard_cmd)######    %=!!!
		mutate_ascii = mutate_ascii % 256

		#ord("a") == 97
		#chr(97) == "a"
		cmd_head = standard_cmd[0 : mutate_position]
		cmd_tail = standard_cmd[(mutate_position + 1) : -1]
		mutate_char = chr((ord(standard_cmd[mutate_position]) + mutate_ascii) % 256)
		mutate_cmd.append(cmd_head + mutate_char + cmd_tail)
		
		mutate_position += 1
		mutate_ascii += mutate_ascii_length
		amount -= 1
	return mutate_cmd


def add_buffer(standard_cmd, seed, amount):
	random.seed(seed)
	pass


def add_format_string(standard_cmd, seed, amount):
	random.seed(seed)
	pass


def mutate_space(standard_cmd, seed, amount):
	random.seed(seed)
	pass


def number(standard_cmd, seed, amount):
	random.seed(seed)
	#not sure
	pass


def mutate_parser(standard_cmd, seed, amount):
	random.seed(seed)
	pass


def mutate_end(standard_cmd, seed, amount):
	random.seed(seed)
	pass