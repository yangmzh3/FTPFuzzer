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


def generate_random_numbers(amount):
	pass


def calculate_loop_length(seed):
	random.seed(seed)
	length = int(round(random.random() * 128.0))
	if length == 0:
		length += 1
	while 128 % length == 0:
		length += 1
	return length


def generate_insert_buffer_data(seed, amount, lengths):
	#mutate ascii length
	mutate_ascii_length = calculate_loop_length(seed)
	
	#mutate ascii char, just assign it the same as length in the begining
	mutate_ascii = mutate_ascii_length

	insert_buffer_data = []
	i = 0################################
	while i < amount:
		insert_length = lengths[i % len(lengths)]
		buffer_data = ""

		j = 0############################
		while j < insert_length:
			buffer_data += chr(mutate_ascii % 128)
			mutate_ascii += mutate_ascii_length
			j += 1
		
		insert_buffer_data.append(buffer_data)
		i += 1
	return insert_buffer_data


def bit_flip(standard_cmd, seed, amount):
	#mutate position of cmd
	mutate_position = 0

	#mutate ascii length of loop
	mutate_ascii_length = calculate_loop_length(seed)

	#mutate startup position's ascii value, just assign it the same as length of loop
	mutate_ascii = mutate_ascii_length

	mutate_cmd = []
	
	while amount > 0:
		mutate_position %= len(standard_cmd)
		mutate_ascii %= 128

		#ord("a") == 97
		#chr(97) == "a"
		cmd_head = standard_cmd[0 : mutate_position]
		cmd_tail = standard_cmd[(mutate_position + 1) : len(standard_cmd)]
		mutate_char = chr((ord(standard_cmd[mutate_position]) + mutate_ascii) % 128)
		print(mutate_char)##################
		mutate_cmd.append(cmd_head + mutate_char + cmd_tail)
		
		mutate_position += 1
		mutate_ascii += mutate_ascii_length
		amount -= 1
	return mutate_cmd


def buffer_overflow(standard_cmd, seed, amount):
	random.seed(seed)
	insert_length = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
	s = generate_insert_buffer_data(seed, amount, insert_length)
	

def format_string(standard_cmd, seed, amount):
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