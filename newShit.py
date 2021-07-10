#!/usr/bin/env python3

"""
def convert():
	celsius = eval(input("Enter celsius: "))
	fahrenheight = 9/5 * celsius + 32
	print("the fahrenheight temp is", fahrenheight)

convert()
"""

def main():
	print("This program illustrates a chaotic function")
	x = float(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x= 3.9 * x * (1 - x)
		print(x)
main()