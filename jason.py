#!/usr/bin/env python3

fname = "romeo.txt"
file = open(fname)
lst  = list()
for line in file.readlines():
	print(line.rstrip())
