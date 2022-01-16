#!/usr/bin/env python3

"""
fname = "romeo.txt"
file = open(fname)
lst  = list()
for line in file.readlines():
	print(line.rstrip())
"""


from random import randint


for _ in range(1,10):
	value = randint(1,10)
	print(value)