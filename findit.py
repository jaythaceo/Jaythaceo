#!/usr/bin/env python3
"""
Tower of Hanoi!
"""
"""
def hanoi(n, p1, p2, p3):
	# Move n discs to move this step
	if n == 0:
		return

	global count
	count += 1

	# Move n-1 discs from p1 to p2
	hanoi(n-1,p1,p3, p2)

	if p1:
		p3.append(p1.pop())
		print(a,b,c)

	hanoi(n-1, p2,p1,p3)

n = 3
a = list(range(n,0,-1))
b, c = [], []

print(a,b,c)
count = 0
hanoi(n, a,b,c)
print(count)
"""

fname = 'romeo.txt'
try:
	fhand =open(fname)
except:
	print("File cannot be opened", fname)
	exit()

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1

print(counts)
